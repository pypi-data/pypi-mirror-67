#!/usr/bin/env python
"""
Summarize HyPhy selection analyses for a gene from JSON files

    SLAC (required)
    FEL  (required)
    MEME (required)
    PRIME (optional)

Author:
    Sergei L Kosakovsky Pond (spond@temple.edu)

Version:
    v0.0.1 (2020-03-23)


"""

import sys
import json
import re
import datetime
import os
import math, csv
from   os import  path
from   Bio import SeqIO
import operator


def get_location (v, country_to_sub):
    if 'country' in v['location']:
        country_to_sub[v['location']['country']] = v['location']['subregion']
        return v['location']['country']
    if 'subregion' in v['location']:
        country_to_sub[v['location']['subregion']] = v['location']['subregion']
        return v['location']['subregion']
    return None


def compute_site_MAF (site, counts_by_site, source = None):
    variants = source[site] if source else counts_by_site [site]
    if len (variants):
        total = sum (variants.values())
        majority = max (variants.values()) / total
        return 1-majority
    return 0

def compute_site_entropy (site, source = None):
    variants = source[site] if source else counts_by_site [site]
    total = sum (variants.values())
    return -sum ([k/total * math.log (k/total,2) for k in variants.values()])


def compute_JH (timing, min_date, max_date):
    #print (timing, file = sys.stderr)
    residue_counts = {}
    mafs_by_date   = {}
    date_cutoff    = min_date + datetime.timedelta(days = 45)
    
    for residue, dates in timing.items():
        residue_counts [residue ] = 0
        for key, value in dates.items():
           #this_date =  datetime.datetime.strptime (key[0], "%Y%m%d")
           this_date = key[0]
           if this_date not in mafs_by_date:
              mafs_by_date [this_date]= {}
           if residue not in mafs_by_date[this_date]:
                mafs_by_date [this_date][residue] = 0
           mafs_by_date[this_date][residue] += value
           if datetime.datetime.strptime (key[0], "%Y%m%d") <= date_cutoff:
                residue_counts[residue] += value
            
    consensus = max(residue_counts.items(), key=operator.itemgetter(1))[0]
    mafs = []
    
    for date, counts in mafs_by_date.items():
        all = sum (counts.values())
        minority = sum ([v for k, v in counts.items() if k != consensus])
        #print (all, minority, counts, [v for k, v in counts.items() if k != consensus], file = sys.stderr)
        mafs.append ([date, minority/all])
  
    bin_count = math.ceil ((max_date - min_date).days/10)
    values_by_bins = [[] for k in range (bin_count)]
    unique_values = set ()
    for v in mafs:
        bin = (datetime.datetime.strptime (v[0], "%Y%m%d")  - min_date).days // 10
        values_by_bins[bin].append (v[1])
        unique_values.add (v[1])
    
    contingency_table = [[0 for k in range (bin_count)] for v in unique_values]
    value_to_index = {}
    for i,v in enumerate (sorted (list(unique_values))):
        value_to_index[v] = i
    
    for i,bin in enumerate (values_by_bins):
        for v in bin:
            contingency_table[value_to_index[v]][i] += 1
           
    value_count = len (unique_values) 
    if value_count == 1:
        return 0.
    row_sums = [sum (row) for row in contingency_table]
    column_sums = [sum ([row[j] for row in contingency_table]) for j in range (bin_count)]
    N = sum (row_sums)
    P = 0
    Q = 0
    
    r3 = sum ([k*k*k for k in row_sums])
    r2 = sum ([k*k for k in row_sums])
    c3 = sum ([k*k*k for k in column_sums])
    c2 = sum ([k*k for k in column_sums])
    
    
    varS = (2.*(N*N*N-r3-c3)+3.*(N*N-r2-c2)+5*N) / 18. + (r3-3*r2+2*N)*(c3-3*c2+2*N)/(9.*N*(N-1)*(N-2)) + (r2-N)*(c2-N)/(2.*N*(N-1))
 
   
    for i,bin in enumerate (values_by_bins):
        for v in bin:
            for j in range (i+1,bin_count):
                for e in values_by_bins[j]:
                    if e < v:
                        Q += 1
                    elif e > v:
                        P += 1
            
    Z = (P-Q) / math.sqrt (varS)            
    return Z


def summary(import_settings):
    db = json.load (import_settings.database)
    dups = json.load (import_settings.duplicates)

    sequences_with_dates = {}
    sequences_with_locations = {}
    country_to_sub = {}

    now      = datetime.datetime.now()
    min_date = now
    max_date = datetime.datetime (1900,1,1)

    for id, record in db.items():
        try:
            date_check = datetime.datetime.strptime (record['collected'], "%Y%m%d")
            if date_check.year < 2019 or date_check.year == 2019 and date_check.month < 10 or date_check >= now: 
                continue
            if date_check < min_date:
                min_date = date_check
            if date_check > max_date:
                max_date = date_check
            sequences_with_dates[id] = record['collected']
            sequences_with_locations[id] = get_location (record, country_to_sub)
        except Exception as e:
            pass
            
    date_dups     = {}

    maf_writer = None

    if import_settings.mafs:
        try:
            maf_file = open (import_settings.mafs, "r+")
            maf_writer = csv.writer (maf_file)
            maf_file.seek (0,2)
        except FileNotFoundError as fnf:
            maf_file = open (import_settings.mafs, "w")
            maf_writer = csv.writer (maf_file)
            maf_writer.writerow (["Gene","Site","aa","count","freq","total"])
        
    evo_writer = None  

    if import_settings.evolutionary_csv:
        try:
            evo_file = open (import_settings.evolutionary_csv, "r+")
            evo_writer = csv.writer (evo_file)
            evo_file.seek (0,2)
        except FileNotFoundError as fnf:
            evo_file = open (import_settings.evolutionary_csv, "w")
            evo_writer = csv.writer (evo_file)
            evo_writer.writerow (["Gene","Site","Codon","Count","Observed","Predicted","Mostlikely"])
            

    evo_annotation = None

    if import_settings.evolutionary_annotation:
        evo_annotation = json.load (import_settings.evolutionary_annotation)
        if import_settings.evolutionary_fragment not in evo_annotation:
            evo_annotation = None
        else:
            evo_annotation = evo_annotation[import_settings.evolutionary_fragment]



    for seq, copies in dups.items():
        date_collection = {}
        location_collection = []
        for cp in copies.values():
            if cp[:3] == 'epi': # Nick mod
                cpv = "_".join (cp.split ('_')[:3])
            else:
                cpv = cp.split ('_')[0]
            if cpv in sequences_with_dates:
                cdate = sequences_with_dates[cpv]
                location = sequences_with_locations[cpv]
                
                try: # Nick mod
                    tag = (cdate, location,db[cpv]['age'],db[cpv]['gender'])
                except:
                    tag = (cdate, location,None,None) 
     
                if not tag in date_collection:
                    date_collection[tag] = 1
                else:
                    date_collection[tag] += 1
                
                    
        date_dups[seq] = date_collection   
     
    slac = json.load (import_settings.slac)
    fel  = json.load (import_settings.fel)
    meme = json.load (import_settings.meme)

    if import_settings.prime:
        prime  = json.load (import_settings.prime)
    else:
        prime = None
        
    ref_seq_map = None
    ref_seq_re = re.compile ("^NC")

    for seq_record in SeqIO.parse(import_settings.coordinates, "fasta"):
        seq_id   = seq_record.description
        if ref_seq_re.search (seq_id):
            ref_seq = str(seq_record.seq).upper()
            i = 0
            c = 0
            ref_seq_map = []
            while i < len (ref_seq):
                ref_seq_map.append (c)
                if ref_seq[i:i+3] != '---':
                    c += 1
                i+=3
            break
            
    if ref_seq_map is None:
        raise Exception ("Misssing reference sequence for coordinate mapping")

        
    # compile the list of sites that are under selection by either MEME or FEL

    site_list = {}
    sequences = slac["input"]["number of sequences"]
    sites = slac["input"]["number of sites"]
    tree = slac["input"]["trees"]["0"]
    branch_lengths = {}

    L = 0


    variants_by_site       = [{} for k in range (sites)]
    aa_variants_by_site    = [{} for k in range (sites)]
    counts_by_site         = [{} for k in range (sites)]
    aa_counts_by_site      = [{} for k in range (sites)]

            
        
    aa_letters = set ("ACDEFGHIKLMNPQRSTVWY")

    for b,v in slac["tested"]["0"].items():
        branch_lengths[b] = slac["branch attributes"]["0"][b]["Global MG94xREV"]
        if v == "test":
            L += slac["branch attributes"]["0"][b]["Global MG94xREV"]
        else:
            for k in range (sites):
                codon = slac["branch attributes"]["0"][b]["codon"][0][k]
                if codon != '---':
                    if codon not in variants_by_site[k]:
                        variants_by_site[k][codon] = 1
                        counts_by_site[k][codon] = len (dups[b])
                    else:
                        variants_by_site[k][codon] += 1
                        counts_by_site[k][codon] += len (dups[b])
                    aa = slac["branch attributes"]["0"][b]["amino-acid"][0][k]
                    if aa in aa_letters:
                        if aa not in aa_variants_by_site[k]:
                            aa_variants_by_site[k][aa] = 1
                            aa_counts_by_site[k][aa] = len (dups[b])
                        else:
                            aa_variants_by_site[k][aa] += 1
                            aa_counts_by_site[k][aa] += len (dups[b])
                    
     
                              
            
    variant_count_total = 0
    variant_count_NS    = 0
            
    valid_nucs = set (["A","C","G","T"])       
        
    for i, row in enumerate (fel["MLE"]["content"]["0"]):
        if row[0] + row[1] > 0:
            maf = compute_site_MAF (i, counts_by_site)
            if maf_writer:
                ##print (variants_by_site[i], file = sys.stderr)
                total = sum (aa_counts_by_site[i].values())
                for aa, count in aa_counts_by_site[i].items():
                    maf_writer.writerow ([import_settings.evolutionary_fragment, "%d" % (ref_seq_map[i] + 1), aa, "%d" % count, "%g" % (count/total), "%d" % total])
                #maf_writer.writerow ([import_settings.evolutionary_fragment, "%d" % (ref_seq_map[i] + 1), "%g" % maf, "%g" % compute_site_MAF (i, aa_counts_by_site), "%g" % compute_site_entropy (i), "%g" % compute_site_entropy (i,aa_counts_by_site), "%g" % meme["MLE"]["content"]["0"][i][6]])
            
            if evo_writer and evo_annotation:
                check_key = "%d" % ref_seq_map[i]
                if evo_annotation and check_key in evo_annotation:
                    total = sum (counts_by_site[i].values())
                    for codon, freq in counts_by_site[i].items():
                        if codon[0] in valid_nucs and codon[1] in valid_nucs and codon[2] in valid_nucs:
                            evo_writer.writerow ([import_settings.evolutionary_fragment, "%d" % (ref_seq_map[i] + 1), codon, "%g" % freq, "%g" % (freq/total), 
                                                  "%g" % (evo_annotation[check_key][codon] if codon in evo_annotation[check_key] else 1e-8), max(evo_annotation[check_key].items(), key=operator.itemgetter(1))[0] ])
                
                
                
            if row[4] < import_settings.pvalue :
                site_list[i] = {'fel' : row[4], 'kind' : 'positive' if row[1] > row[0] else 'negative', 'MAF' : maf}
            else:
                if maf >= import_settings.MAF:
                    site_list[i] = {'fel' : row[4],  'MAF' : maf}
            
        
    for i, row in enumerate (meme["MLE"]["content"]["0"]):
        if row[6] < import_settings.pvalue or i in site_list:
            if i in site_list:
                site_list[i]['meme'] = row[6]
                site_list[i]['meme-fraction'] = row[4]
            else:
                site_list[i] = {'meme' : row[6], 'fel' : fel["MLE"]["content"]["0"][i][4], 'meme-fraction' : row[4], 'MAF' : compute_site_MAF (i, counts_by_site)}


        

    for site in site_list:
        site_list[site]['meme-branches'] = meme["MLE"]["content"]["0"][site][7]
        site_list[site]['substitutions'] = [slac["MLE"]["content"]["0"]['by-site']['RESOLVED'][site][2],slac["MLE"]["content"]["0"]['by-site']['RESOLVED'][site][3]]
        labels      = {}
        evo_composition = {}
        timing      = {}
        ''' 
            for each amino acid, this will record "date" : count for when they were sampled
            timing -> 
                "residue" ->
                    "date" -> count
        '''
        check_key           = "%d" % ref_seq_map[site]
        evo_site_annotation      = evo_annotation[check_key] if evo_annotation and check_key in evo_annotation else None
        
        for node,value in slac["branch attributes"]["0"].items():
            if "amino-acid" in value:
                aa_value    = value["amino-acid"][0][site]
                codon_value = value["codon"][0][site]
                
                if len (aa_value) == 1 and evo_site_annotation:
                    if codon_value not in evo_composition:
                        try:
                            evo_composition[codon_value] = {
                                "support" : evo_annotation[check_key][codon_value], "aa" : aa_value
                                }
                        except Exception as e:
                            evo_composition[codon_value] = {
                                "support" : 0.0, "aa" : aa_value
                                }
                                
                
                if node in date_dups:
                    if aa_value not in timing:
                        timing [aa_value] = {}
                    for dt, cnt in date_dups[node].items():
                        if not dt in timing [aa_value]:
                            timing [aa_value][dt] = cnt
                        else:
                            timing [aa_value][dt] += cnt
                 
                labels[node] = [aa_value,value["codon"][0][site],value["nonsynonymous substitution count"][0][site],value["synonymous substitution count"][0][site]]
        
        site_list[site]['composition'] = aa_counts_by_site[site]
        site_list[site]['labels'] = labels
        if len (evo_composition):
            site_list[site]['evolutionary_support']     = evo_composition
            site_list[site]['evolutionary_predictions'] = evo_site_annotation
            site_list[site]['counts'] = counts_by_site 
            print ("Site %d" % site, file = sys.stderr)
            print ("Codon\tAmino-Acid\tFrequency\tSupport", file = sys.stderr)
            all_count = sum (counts_by_site[site].values())
            for codon, support in evo_composition.items():
                codon_freq = [v for k,v in counts_by_site[site].items() if k == codon]
                if len (codon_freq):
                    print ("%s\t%s\t%.3g\t%.3g" % (codon,support["aa"],[v for k,v in counts_by_site[site].items()if k == codon][0]/all_count,support["support"]), file = sys.stderr)
            #print (site, evo_composition,aa_counts_by_site[site], file = sys.stderr)
        
        timing_as_array = {}
        
        for aa, t in timing.items():
            timing_as_array [aa] = [[k[0],k[1],country_to_sub[k[1]],v,k[2],k[3]] for k, v in timing[aa].items()]
        
        site_list[site]['timing'] = timing_as_array
        site_list[site]['trend'] = compute_JH (timing, min_date, max_date)
        
        if prime:
            site_list[site]['prime'] = []
            prime_row = prime["MLE"]["content"]["0"][site]
            prime_headers = prime["MLE"]["headers"]
            for idx in [5,7,10,13,16,19]:
                if prime_row[idx] <= import_settings.pvalue :
                   if idx == 5:
                        site_list[site]['prime'].append (['Overall', prime_row[idx], 0])
                   else:
                        site_list[site]['prime'].append ([prime_headers[idx][1].replace ('p-value for non-zero effect of ',''), prime_row[idx], prime_row[idx-1]])
                        
            
    json_out = {
        'sequences' : sequences,
        'bl' : branch_lengths,
        'total sequences' : sum ([len (k) for k in dups.values()]),
        'aminoacid variant sites' : [v for v in aa_variants_by_site if len (v) > 1 and len ([c for c in v.values() if c>1]) > 1],
        'all variant sites' : [v for v in variants_by_site if len (v) > 1 and len ([c for c in v.values() if c>1]) > 1],
        'any variation' : len ([v for v in variants_by_site if len (v) > 1]),
        'sites' : sites,
        'tree' : tree,
        'MAF' : import_settings.MAF,
        'L' : L,
        'p' : import_settings.pvalue,
        'selection' : site_list,
        'map' : ref_seq_map,
        'dN/dS' : {
            'internal' :  meme["fits"]["Global MG94xREV"]["Rate Distributions"]["non-synonymous/synonymous rate ratio for *test*"],
            'leaves'   :  meme["fits"]["Global MG94xREV"]["Rate Distributions"]["non-synonymous/synonymous rate ratio for *background*"]
        }
    }

    with open('summary.json', 'w') as file:
        json.dump (json_out, file, sort_keys = True, indent = 1)
        

