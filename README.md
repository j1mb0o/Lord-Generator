# Lord-Generator

## Setup
To create the virual environemtn `miniconda` was used and `Python 3.11` version.

```bash
conda create -n [NAME] python=3.11
```

To install the required packages:
```bash
conda activate [NAME]
pip install markovify langchain langchain-ollama matplotlib 
```

## Project structure
The project is structured with 4 directiories.
*  `data`:  contains the data used
* `generation`:  has the code to generate the poems 
* `evaluation`: code used to conduct the evaluation study and create accuracy metrics
* `submition`: has the presentetion form of the poems (1 image and 2 audio files), for every file there is another one `.txt` with the same name. For the audio files it is the poem that is being narrated, and for the image it is the prompt that was used in the `midjurney` model.