# YOUR CODE HERE
X_1 = pd.DataFrame()  # dataframe to hold new features

X_1["LivLotRatio"] = df.GrLivArea/df.LotArea
X_1["Spaciousness"] = (df.FirstFlrSF + df.SecondFlrSF)/df.TotRmsAbvGrd
X_1["TotalOutsideSF"] = df.WoodDeckSF + df.OpenPorchSF + df.EnclosedPorch + df.Threeseasonporch + df.ScreenPorch


# Check your answer
q_1.check()

# YOUR CODE HERE
# One-hot encode BldgType. Use `prefix="Bldg"` in `get_dummies`
X_2 = pd.get_dummies(df.BldgType, prefix = "Bldg")
# Multiply
X_2 = X_2.mul(df.GrLivArea, axis = 0)


# Check your answer
q_2.check()

X_3 = pd.DataFrame()

# YOUR CODE HERE
components = ["WoodDeckSF", "OpenPorchSF", "EnclosedPorch", "Threeseasonporch", "ScreenPorch"]
X_3["PorchTypes"] = df[components].gt(0).sum(axis = 1)


# Check your answer
q_3.check()

X_4 = pd.DataFrame()

# YOUR CODE HERE
X_4["MSClass"] = (
    df["MSSubClass"]
    .str
    .split("_",n = 1, expand = True)[0]
)

# Check your answer
q_4.check()

X_5 = pd.DataFrame()

# YOUR CODE HERE
X_5["MedNhbdArea"] = df.groupby("Neighborhood")["GrLivArea"].transform("median")

# Check your answer
q_5.check()


