#!/usr/bin/env bash
whoami
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh --no-check-certificate
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
echo $HOME
conda config --set always_yes yes --set changeps1 no
conda update conda
pip install --upgrade pip

conda install -c pyviz panel ipython jupyter hvplot scikit-learn