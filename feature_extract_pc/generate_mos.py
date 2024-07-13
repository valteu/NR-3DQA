import pandas as pd
import numpy as np

# Assuming you have the same filenames as in features.csv
features_df = pd.read_csv("features.csv", index_col=0)
filenames = features_df.index

# Generate random MOS scores (for demonstration)
mos_scores = np.random.uniform(5, 10, size=len(filenames))

mos_df = pd.DataFrame({
    'filename': filenames,
    'score': mos_scores
})

mos_df.to_csv("mos.csv", index=False)
