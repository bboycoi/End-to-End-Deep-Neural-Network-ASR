

## Project Overview

In this project builds a deep neural network that functions end-to-end automatic speech recognition (ASR) pipeline!  

This is an ongoing project, we are adding language model to the pipeline.

![ASR Pipeline](/images/VUI_flow.png)

## Project Instructions

The Notebook `vui.ibnpy` is the Main procedure, it is self-explained and is a good place to start.

### Local  Setup

You should run this project with GPU acceleration for best performance.

1. Install TensorFlow.
	- Option 1: __To install TensorFlow with GPU support__, follow [the guide](https://www.tensorflow.org/install/) to install the necessary NVIDIA software on your system.  If you are using an EC2 GPU instance, you can skip this step and only need to install the `tensorflow-gpu` package:
	```
	pip install tensorflow-gpu==1.1.0
	```
	- Option 2: __To install TensorFlow with CPU support only__,
	```
	pip install tensorflow==1.1.0
	```

2. Install a few Requires packages.
```
pip install -r requirements.txt
```

3. Switch [Keras backend](https://keras.io/backend/) to TensorFlow.
	- __Linux__ or __Mac__: 
	```
	KERAS_BACKEND=tensorflow python -c "from keras import backend"
	```

4. Obtain the `libav` package.
	- __Linux__: `sudo apt-get install libav-tools`

5. Obtain the appropriate dataset, and convert all flac files to wav format. This works with data directories that are organized like LibriSpeech:
data_directory/group/speaker/[file_id1.wav, file_id2.wav, ..., speaker.trans.txt]
Where speaker.trans.txt has in each line, file_id transcription
	- __Linux__ or __Mac__: 
	```
	mv flac_to_wav.sh $data_folder$
	cd $data_folder$
	./flac_to_wav.sh
	```

5. Create JSON files corresponding to the train and validation datasets.
```
cd ..
python create_desc_json.py $data_folder$ train_corpus.json
python create_desc_json.py $data_folder$ valid_corpus.json
```


## TODO!

#### (1) Add a Language Model to the Decoder

The performance of the decoding step can be greatly enhanced by incorporating a language model.  


#### (3) Try out Different Audio Features

Train a network that uses raw audio waveforms!

