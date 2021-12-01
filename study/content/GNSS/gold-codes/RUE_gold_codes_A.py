# -*- coding: utf-8 -*-

"""
Rechneruebung GNSS Gold Codes

Author: Lehrstuhl für Informationstechnik mit dem Schwerpunkt Kommunikationselektronik
Last edited: 19.09.2019
"""

import numpy as np
from matplotlib import pyplot as plt

def calculate_gold_code(PRN, gold_code_length=None): #!DONT REPLACE NONE!
    ### To Do: replace None ###
    
    size_shift_register = 10 #Size of the shift registers
    
    if gold_code_length is None: #!DONT REPLACE NONE!
        gold_code_length = 2**size_shift_register-1
        
    if PRN == 5:
        phase_selector = np.array([1, 9]) #Get from ICD200c.pdf
    elif PRN == 19:
        phase_selector = np.array([3, 6]) #Get from ICD200c.pdf
    elif PRN == 25: 
        phase_selector = np.array([5, 7]) #Get from ICD200c.pdf
    else:
        print('PRN not valid. Using PRN19.')
        phase_selector = np.array([3, 6]) #Get from ICD200c.pdf
    
    taps_1 = np.array([3, 10]) #cf tasks
    taps_2 = np.array([2, 3, 6, 8, 9, 10]) #cf. tasks
    
    register_1 = np.ones((size_shift_register))
    register_2 = np.ones((size_shift_register))
    
    gold_code =  np.ones((gold_code_length))
    
    for i in range(gold_code_length): 
        feedback_1 = sum(register_1[taps_1-1]) % 2  #Calculate feedbacks, cf. tasks
        feedback_2 = sum(register_2[taps_2-1]) % 2  #remember python indexing starts at 0 -> taps
        
        G_2i = sum(register_2[phase_selector-1]) % 2 #cf. tasks
        G_1 = register_1[-1] #cf. tasks
        
        gold_code[i] = (G_2i + G_1) % 2 #cf. tasks
        
        register_1 = np.roll(register_1, 1) #shift, np.roll
        register_1[0] = feedback_1 #feedback
        
        register_2 = np.roll(register_2, 1) #shift, np.roll
        register_2[0] = feedback_2 #feedback
        
    return gold_code
 
def octal_chips(chips):
    value = 0
    for i in range(chips.shape[0]):
        value += (2**i) * chips[-1-i]
    return oct(int(value))
        
def cyclic_correlation(sequence_1, sequence_2):
    sequence_length = sequence_1.shape[0]
    max_shift = sequence_length
    correlation = np.zeros((2*sequence_length+1))
    for shift in range(-max_shift, max_shift+1, 1):
        sequence_2_shifted = np.roll(sequence_2, -shift)
        correlation[shift+max_shift] = np.correlate(sequence_1[:], sequence_2_shifted[:])   
    correlation = correlation / sequence_length
    return correlation   
    
def uni_to_bi(sequence):
    return (-2 * sequence + 1)   
    
if __name__ == '__main__':
    ### To Do: replace None ###
    
#Task a
    
    PRN_19 = calculate_gold_code(19)
    print(PRN_19)
    
#    fig_1, ax_1 = plt.subplots()
#    fig_1.suptitle('First 16 chips of PRN 19', fontsize=12)
#    ax_1.stem(PRN_19[:16], linefmt='b-', markerfmt='bo', basefmt=' ', label='PRN19')
#    ax_1.set_xlabel('Chip')
#    ax_1.set_ylabel('Value')
#    ax_1.legend()
#    ax_1.grid()
#    plt.show()
#    
#    fig_2, ax_2 = plt.subplots()
#    fig_2.suptitle('Last 16 chips of PRN 19', fontsize=12)
#    ax_2.stem(PRN_19[-16:], linefmt='r-', markerfmt='ro', basefmt=' ', label='PRN19')
#    ax_2.set_xlabel('Chip')
#    ax_2.set_ylabel('Value')
#    ax_2.legend()
#    ax_2.grid()
#    plt.show()
    
#Task b, c, d
    
    PRN_19_2046 = calculate_gold_code(19, 2046)
    
    PRN_19_first = PRN_19_2046[:1023] #PRN 19 from Chip 1 to 1023
    PRN_19_second = PRN_19_2046[1023:]  #PRN 19 from Chip 1024 to 2046
    PRN_19_diff = PRN_19_second-PRN_19_first #Show if theres any difference between PRN_19_first and PRN_19_second
    
#    fig_3, ax_3 = plt.subplots()
#    fig_3.suptitle('PRN 19', fontsize=12)
#    ax_3.stem(PRN_19_first, linefmt='b-', markerfmt='bo', basefmt=' ', label='PRN19 1 to 1023')
#    ax_3.stem(PRN_19_second, linefmt='r--', markerfmt='ro', basefmt=' ', label='PRN19 1024 to 2046')
#    ax_3.stem(PRN_19_diff, linefmt='g:', markerfmt='gx', basefmt=' ', label='Difference')
#    ax_3.set_xlabel('Chip')
#    ax_3.set_ylabel('Value')
#    ax_3.legend()
#    ax_3.grid()
#    plt.show()
#    
    PRN_19 = calculate_gold_code(19)
    octal_19 = octal_chips(PRN_19[:10])
    print('PRN 19 first 10 chips octal: ', octal_19) #Check output with ICD200c.pdf
    
    PRN_25 = calculate_gold_code(25)
    octal_25 = octal_chips(PRN_25[:10])
    print('PRN 25 first 10 chips octal: ', octal_25)
    
    PRN_5 = calculate_gold_code(5)
    octal_5 = octal_chips(PRN_5[:10])
    print('PRN 5 first 10 chips octal: ', octal_5)
    
#Task e to l
    
    PRN_19 = calculate_gold_code(19)
    PRN_19 = uni_to_bi(PRN_19)
    correlation_19_19 = cyclic_correlation(PRN_19, PRN_19)
    
    PRN_19_200 = np.roll(PRN_19, 200) #np.roll
    correlation_19_19_d200 = cyclic_correlation(PRN_19, PRN_19_200)
    
    PRN_25 = calculate_gold_code(25)
    PRN_25 = uni_to_bi(PRN_25)
    correlation_19_25 = cyclic_correlation(PRN_19, PRN_25)
    
    PRN_5 = calculate_gold_code(5)
    PRN_5 = uni_to_bi(PRN_5)
    correlation_19_5 = cyclic_correlation(PRN_19, PRN_5)
    
    PRN_5_75 = np.roll(PRN_5, 75) #np.roll
    PRN_19_350 = np.roll(PRN_19, 350) #np.roll
    PRN_25_905 = np.roll(PRN_25, 905) #np.roll
    
    Signal_1 = PRN_19_350 + PRN_25_905 + PRN_5_75 #add PRNs
    correlation_19_Signal_1 = cyclic_correlation(PRN_19, Signal_1)
     
    fig_4, ax_4 = plt.subplots()
    fig_4.suptitle('ACF / CCF PRN 19', fontsize=12)
    
    #ax_4.stem(np.arange(-1023, 1024, 1), correlation_19_19,  linefmt='b-', markerfmt='bo', basefmt=' ', label='ACF PRN19')
    #ax_4.stem(np.arange(-1023, 1024, 1), correlation_19_19_d200, linefmt='r:', markerfmt='ro', basefmt=' ', label='CCF PRN19 PRN19Delay200')
    #ax_4.stem(np.arange(-1023, 1024, 1), correlation_19_25,  linefmt='k-.', markerfmt='ko', basefmt=' ', label='CCF PRN19 PRN25')
    #ax_4.stem(np.arange(-1023, 1024, 1), correlation_19_5,  linefmt='y--', markerfmt='yo', basefmt=' ', label='CCF PRN19 PRN5')
    #ax_4.stem(np.arange(-1023, 1024, 1), correlation_19_Signal_1, linefmt='g-', markerfmt='go', basefmt=' ', label='CCF PRN19 Signal_1')
    
    ax_4.set_xlabel('Delay')
    ax_4.set_ylabel('Correlation')
    ax_4.legend()
    ax_4.grid()
    plt.show()
    
    noise = np.random.normal(0.0, 4.0, size=1023)
    
    fig_5, axes = plt.subplots(2, 2, sharex='all', sharey='all')
    fig_5.suptitle('PRNs and Noise', fontsize=12)
    
    axes[0, 0].stem(noise, linefmt='r--', markerfmt='ro', basefmt=' ', label='Noise')
    axes[0, 1].stem(PRN_5_75, linefmt='g--', markerfmt='go', basefmt=' ', label='PRN5')
    axes[1, 0].stem(PRN_19_350, linefmt='b--', markerfmt='bo', basefmt=' ', label='PRN19')
    axes[1, 1].stem(PRN_25_905, linefmt='k--', markerfmt='ko', basefmt=' ', label='PRN25')
    
    axes[0, 0].grid()
    axes[0, 1].grid()
    axes[1, 0].grid()
    axes[1, 1].grid()
    axes[1, 0].set_xlabel('Chip')
    axes[1, 1].set_xlabel('Chip')
    axes[1, 0].set_ylabel('Value')
    axes[0, 0].set_ylabel('Value')
    plt.show()
    
    Signal_2 = PRN_19_350 + PRN_25_905 + PRN_5_75 + noise# add noise and PRNs
    correlation_19_Signal_2 = cyclic_correlation(PRN_19, Signal_2)
    
    correlation_19_sign_Signal_2 = cyclic_correlation(PRN_19, np.sign(Signal_2)) #use np.sign
    
    fig_6, (ax_6_1, ax_6_2) = plt.subplots(2, 1, sharex='all', sharey='all')
    fig_6.suptitle('Signal 2', fontsize=12)
    
    ax_6_1.stem(Signal_2, linefmt='g-', markerfmt='go', basefmt=' ', label='Signal_2')
    ax_6_1.set_ylabel('Measurement')
    ax_6_1.legend()
    ax_6_1.grid()
    
    ax_6_2.stem(np.sign(Signal_2), linefmt='r-', markerfmt='ro', basefmt=' ', label='sign(Signal_2)') #use np.sign
    ax_6_2.set_ylabel('Measurement')
    ax_6_2.set_xlabel('Chip')
    ax_6_2.legend()
    ax_6_2.grid()
    plt.show()
    
    fig_7, (ax_7_1, ax_7_2) = plt.subplots(2, 1, sharex='all', sharey='all')
    fig_7.suptitle('CCF PRN 19, Signal 2', fontsize=12)
    
    ax_7_1.stem(np.arange(-1023, 1024, 1), correlation_19_Signal_2, linefmt='g-', markerfmt='go', basefmt=' ', label='CCF PRN19 Signal_2')
    ax_7_1.set_ylabel('Correlation')
    ax_7_1.legend()
    ax_7_1.grid()
    
    ax_7_2.stem(np.arange(-1023, 1024, 1), correlation_19_sign_Signal_2, linefmt='r-', markerfmt='ro', basefmt=' ', label='CCF PRN19 sign(Signal_2)')
    ax_7_2.set_ylabel('Correlation')
    ax_7_2.set_xlabel('Delay')
    ax_7_2.legend()
    ax_7_2.grid()
    plt.show()
    
    max_2 = np.amax(abs(correlation_19_Signal_2))
    idx_max_2 =  np.where(abs(correlation_19_Signal_2) == max_2)
    PN_2 = np.var(correlation_19_Signal_2[idx_max_2[0][0]+1:idx_max_2[0][1]-1]) 
    SNR_2 = 10*np.log10(max_2**2 / PN_2)
    print('SNR Correlation Signal_2 in dB: ', SNR_2)
    
    max_s2 = np.amax(abs(correlation_19_sign_Signal_2))
    idx_max_s2 =  np.where(abs(correlation_19_sign_Signal_2) == max_s2)
    PN_s2 = np.var(correlation_19_sign_Signal_2[idx_max_s2[0][0]+1:idx_max_s2[0][1]-1]) 
    SNR_s2 = 10*np.log10(max_s2**2 / PN_s2)
    print('SNR Correlation sign(Signal_2) in dB: ', SNR_s2)
