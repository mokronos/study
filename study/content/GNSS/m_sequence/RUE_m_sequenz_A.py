# -*- coding: utf-8 -*-

"""
Rechneruebung GNSS m-Sequenzen

Author: Lehrstuhl für Informationstechnik mit dem Schwerpunkt Kommunikationselektronik
Last edited: 19.09.2019
"""

import numpy as np
from matplotlib import pyplot as plt

def calculate_m_sequence(m, taps, init_register):
    ### ToDo: replace None ###
    
    sequence_length = 2**m-1 #calculate the length of the m-sequence
    register = init_register #initialize the first register state
    m_sequence = np.zeros((1,sequence_length)) #initialize an empty (zeros) array with the correct size (Hint: np.zeros)
    
    #Task c
    register_states = np.zeros((sequence_length + 1,m)) #initialize an empty array for the register states
    register_states[0,:] = register

    # calculate the m-sequence
    for i in range(sequence_length):
        m_sequence[0,i] = register[len(register)-1] #get the right value for the m-sequence

        fb = 0
        for x in taps:
            fb += register[x-1]

        feedback = fb % 2 #calculate feedback 
        register = np.roll(register,1) #shift register (Hint: np.roll)
        register[0] = feedback #put in feedback
        register_states[i + 1,:] = register

    print(register_states)
    
    return m_sequence ,register_states
    
def check_calculate_m_sequence(m, taps, init_register):
    
    m_sequence,_ = calculate_m_sequence(m, taps, init_register)
    solution = np.array([[1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0]])
    
    if np.array_equal(m_sequence, solution):
        print('Test calculate_m_sequence passed!')
    else:
        print('Test calculate_m_sequence failed!')
    return   
        
def cyclic_correlation(sequence_1, sequence_2):
    ### ToDo: replace None ###
    
    sequence_length = sequence_1.shape[1] #calculate the length of the correlation
    max_shift =  sequence_length-1 #calculate the maxium shift
    correlation = np.zeros((2*sequence_length-1)) #initialize an empty array with the correct size
    
    # calculate the correlation
    for shift in range(-max_shift, max_shift+1, 1): 
        sequence_2_shifted = np.roll(sequence_2, -shift) #shift sequence 2 (Hint: np.roll)
        correlation[shift+max_shift] = np.correlate(sequence_1[0,:], sequence_2_shifted[0,:]) #calculate correlation (Hint: np.correlate)
        
    correlation = correlation / sequence_length #normalization
    return correlation
    
def uni_to_bi(sequence):
    ### ToDo: replace None ###
    return -2 * sequence + 1
    
if __name__ == '__main__':
    
    #Task b 
    
    taps = np.array([1, 4])
    init_register = np.array([1, 1, 0, 1])
    #check_calculate_m_sequence(4, taps, init_register)
    
#    m_sequence, registers = None
#    print("m-sequence: ", None)
#    print("Registers: \n", None)
    
    #Task e 
    
    taps = np.array([2, 4])
    init_register = np.array([0, 0, 0, 1])
    
    #check_calculate_m_sequence(4, taps, init_register)
    #Task g 
    
    taps_1 = np.array([1, 4])
    init_register_1 = np.array([0, 0, 0, 1])
    
    taps_2 = np.array([1, 4])
    init_register_2 = np.array([1, 1, 0, 1])
    
    taps_3 = np.array([2, 4])
    init_register_3 = np.array([0, 0, 0, 1])
    
    taps_4 = np.array([3, 4])
    init_register_4 = np.array([0, 0, 0, 1])
    
    m_sequence_1, registers_1 = calculate_m_sequence(4, taps_1, init_register_1)
    m_sequence_2, registers_2 = calculate_m_sequence(4, taps_2, init_register_2)
    m_sequence_3, registers_3 = calculate_m_sequence(4, taps_3, init_register_3)
    m_sequence_4, registers_4 = calculate_m_sequence(4, taps_4, init_register_4)
    m_sequence_1 = uni_to_bi(m_sequence_1)
    m_sequence_2 = uni_to_bi(m_sequence_2)
    m_sequence_3 = uni_to_bi(m_sequence_3)
    m_sequence_4 = uni_to_bi(m_sequence_4)
    
    correlation_1_1 = cyclic_correlation(m_sequence_1, m_sequence_1) # replace None
    correlation_2_2 = cyclic_correlation(m_sequence_2, m_sequence_2) # replace None
    correlation_3_3 = cyclic_correlation(m_sequence_3, m_sequence_3) # replace None
    correlation_4_4 = cyclic_correlation(m_sequence_4, m_sequence_4) # replace None
    
    fig_1, ax_1 = plt.subplots()
    fig_1.suptitle('Auto Correlation', fontsize=12)
    ax_1.stem(np.arange(-14, 15, 1), correlation_1_1, linefmt='b:', markerfmt='bP', basefmt=' ', label='ACF S1')
    ax_1.stem(np.arange(-14, 15, 1), correlation_2_2, linefmt='g:', markerfmt='g^', basefmt=' ', label='ACF S2')
    ax_1.stem(np.arange(-14, 15, 1), correlation_3_3, linefmt='r:', markerfmt='r*', basefmt=' ', label='ACF S3')
    ax_1.stem(np.arange(-14, 15, 1), correlation_4_4, linefmt='y:',  markerfmt='yx', basefmt=' ', label='ACF S4')
    ax_1.grid()
    ax_1.set_xlabel('Delay')
    ax_1.set_ylabel('Correlation')
    ax_1.legend()
    plt.show()
    
    #Task i 
    
    correlation_1_2 = cyclic_correlation(m_sequence_1, m_sequence_2) # replace None
    correlation_1_3 = cyclic_correlation(m_sequence_1, m_sequence_3) # replace None
    correlation_1_4 = cyclic_correlation(m_sequence_1, m_sequence_4) # replace None
    correlation_2_3 = cyclic_correlation(m_sequence_2, m_sequence_3) # replace None
    correlation_2_4 = cyclic_correlation(m_sequence_2, m_sequence_4) # replace None
    correlation_3_4 = cyclic_correlation(m_sequence_3, m_sequence_4) # replace None
    
    fig_2, ax_2 = plt.subplots()
    fig_2.suptitle('Cross Correlation', fontsize=12)
    ax_2.stem(np.arange(-14, 15, 1), correlation_1_2, linefmt='b:', markerfmt='bP', basefmt=' ', label='CCF S1 S2')
    ax_2.stem(np.arange(-14, 15, 1), correlation_1_3, linefmt='g:',  markerfmt='g^', basefmt=' ', label='CCF S1 S3')
    ax_2.stem(np.arange(-14, 15, 1), correlation_1_4, linefmt='r:', markerfmt='r*', basefmt=' ', label='CCF S1 S4')
    ax_2.stem(np.arange(-14, 15, 1), correlation_2_3, linefmt='y:', markerfmt='yx', basefmt=' ', label='CCF S2 S3')
    ax_2.stem(np.arange(-14, 15, 1), correlation_2_4, linefmt='c:',  markerfmt='co', basefmt=' ', label='CCF S2 S4')
    ax_2.stem(np.arange(-14, 15, 1), correlation_3_4, linefmt='m:', markerfmt='ms', basefmt=' ', label='CCF S3 S4')
    ax_2.grid()
    ax_2.set_xlabel('Delay')
    ax_2.set_ylabel('Correlation')
    ax_2.legend()
    plt.show()
