source create --prefix ./env python=3.7 -y
source activate ./env

source env export > conda.yaml