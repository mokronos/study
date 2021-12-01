# Notes for Paper review
## Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks by Alex Graves, Santiago Fernández, Faustino Gomez, Jürgen Schmidhuder


### Some terms:

- **sequence learning task**: Tasks which can be learned as single steps but are in reality often learned by taking multiple steps at once to simplify the task. e.g.: sounds in speech, typing, playing an instrument, driving a car.

- **unsegmented data**: Data that has no clear indication of where the diffrent segments are. e.g.: soundwaves without clear indication of where the diffrent words of start and end, youtube video without chapter markings, text without spaces between words.

- **sub-word units**: Smaller parts of speech than words. Morphemes, stems and endings. e.g.: un|happy|ly, cat|s

- **recurrent neural network(RNN)**: A type of neural network in which neurons can send information to each other forward through time. This gives these networks memory of the states before which can be used as context for the current state.

- **negative log likelihood**: \(score = - log(p)\), probability in [0,1] --> log(p) negative --> positive through minus --> highest probabilities = lowest score (log(1)=0)

- **Label Error Rate(LER)**: normalised edit distance between outputs and the ground truth. Levenshtein distance is probably used (allows deletion, insertion and substitution). So helro --> hello LER = 1/5 (1 substitution, 5 labels) --> minimises transcription mistakes


### Key Questions:

1. Goals of the paper:
    - solving Problems around the use of RNNs for sequential learning
    - remove need for segmented input data
    - every nuance of a sequence can be determined through one network (double letters, segmentation, recognition)
2. Key elements of new method:
    - RNN outputs probability distribution over the alphabet at each time step --> calculate over possible sequences
    - simplify calculation of sequence probabilities by merging when going over same node
    - training: 
      - data: input sequence always has more or the same samples as output labels
      - loss function easily differentiable --> standard backpropagation through time
3. What Content of the paper is useful?
    - explanation of training data is very clear
    - methods are described well and in detail
    - figure 1 is not well described (no legend)
4. Other references:
    - https://distill.pub/2017/ctc/
    - https://medium.com/deeplearningmadeeasy/negative-log-likelihood-6bd79b55d8b6


### Symbols

| Symbol      | Description | Dimensions   |
| ----------- | ----------- | ------------ |
| \(\textbf{X}\)| input sequence| 1xT, T=time
| \(\textbf{Z}\)| target sequence| 1xU, U=time U\<T
| 


### Architecture

data: audio clips, corresponding transcripts  
goal: align the words/subwords in the transcipt with the audio clips (transform data from unsegmented to segmented  
naive approch: 10 audio signal inputs (timesteps) equal 1 character | issue: varying speed of speech  
ctc: calculating the probability distribution over all possible variations of \(\textbf{Z}\) with a given \(\textbf{X}\).  

data of audio sequence --> split into time steps --> input for RNN(pixels of spectogram/actual values) at first time step --> output is distribution over alphabet of letters/symbols + blank --> repeat for other time steps(with memory of RNN --> multiply probabilities of all variations of characters in a sequence to get a distribution over all sequences --> take the most likely one/look at probabilities  

training: 
 - maxmimum likelihood: minimizing negative log likelihood, better for computers to add than multiply by high/low numbers
 - basic backprpagation through time + gradient-based optimisation algorithms (like adam)
 - dynamic programming/merging alignments to simplify variations of alignments, otherwise way to slow

forward-backward algorithm:
 - goal: efficent way of summing up the probabilities of all the paths corresponding to one labeling sequence (ther are a lot
 - recursivly calculating probabilities of sequences up to certain labels in sequence (prefixes).
inference: 
 - get max probability sequence, \(\underset{Y}{\arg\max} \, p(Y|X)\)
 - also possibly to get max likely alignment at each timestep

 - example:
    - input: "hello" as waveform, must be split up into ms --> length T
    - example alphabet: L = {h,e,l,o,*blank*} (can be any alphabet, so u can group "h","e" together as "he" if it occurs oven in a text)
    - for every timestep:
        - first input "h" in waveform
        - outputs \(y_k^t\) (t=0,k=1-5): {h:0.5, e:0.2, l:0.05, o:0.01, *blank*:0.15}
    - multiply probabilities of timesteps --> calculate probabilies \(p(\pi|x)\) (x=input, \(\pi\)=one specific sequence/path) of sequences:
        - **h** | **e** | **l** | **l** | **o**   p=0.4
        - **h** | **e** | **l** | **o** | *blank*   p=0.3
        - **h** | **e** | *blank* | **l** | **o**   p=0.1
        - ect.
        - sequences are T long --> many *blank*s and same letters after each other
    - remove blanks/multiple letters (decoding) and add the probabilies of the merged sequences --> take sequence with max probability p(l|x) as result --> [hello]
        - (hh_eee__l_lo) = (he_l___l__o) = hello
    - not viable to calculate all --> 2 methods for selection:
        - "best path decoding": just use the most likely before decoding as its easy to compute (its possible that the most likely sequence before "decoding" is not the most likely after merging/decoding aka the final labeling) 
        - "prefix search decoding": takes longer but always finds the best labeling. takes exponentially longer the longer the sequence --> seperation into smaller sequences on blanks that are predicted over a certain threshold (here 99.99%)

random stuff:
 - depending on how much you know about a topic you can help the network part of the system by integrating your knowledge in the selection of the alphabet. If you know more about maschine learning you can instead improve the network part of the system and help it that way. The network can in a way smooth out the interface independent of what the alphabet is.
 - labeling  is focus, neural net + classifier, mention searches only a little bit, forward backward important for training, otherwise too slow




### Questions:

- Abstract is hard to write because the original abstract is already a pretty good summary from the authors (who understand the topic better than me). i feel like i make the abstract worse just to make it different.
- Write about the paper or about the topic of the paper and mention the original paper?
- Include more recent work that stemmed from that paper (maybe from the same authors) or methods that are now used instead of this papers method? or like only research that happened before the paper? (especially for literature review)
    - better in conclusion for future work
- What details to leave out? (probably the main part of my job to figure that out)
- Should the focus be to make it as easy as possible for readers to understand the main structure and method and spare them some more complicated details? or focus on how to implement the method?

- version of paper
