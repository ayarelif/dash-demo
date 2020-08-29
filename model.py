import pickle

with open("./assets/model.pkl","rb") as f:
    model = pickle.load(f)

# Instantiate the model
# infile = open("./assets/model.pkl", "rb")
# model = pickle.load(infile)
# infile.close()