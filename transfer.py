import os
from joblib import Parallel, delayed
counter = os.system('gsutil ls | wc -l') - 1
gslist = os.system('gsutil ls | tail -n+2')
def matrixcopy(var):
   cmd = "gsutil -m rsync -r $(gsutil ls | head -n 1)" + var
   os.system(cmd)

results = Parallel(n_jobs=counter)(delayed(matrixcopy)(var) for var in gslist )
