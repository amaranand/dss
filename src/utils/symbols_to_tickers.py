import os
import pandas as pd
import yaml

INPUT_DIR = "data/raw/nse_indices_components/"        # folder with 8 CSVs
OUTPUT_DIR = "data/processed/stocks/"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ----------------------------------------
# LOAD CSV
# ----------------------------------------
def load_index(name, index_type):
    """
    Returns dataframe with an extra column 'type'
    """
    df = pd.read_csv(os.path.join(INPUT_DIR, f"{name}.csv"))
    df["type"] = index_type
    return df


# ----------------------------------------
# Convert DataFrame → YAML symbols
# ----------------------------------------
def df_to_yaml(df):
    symbols = []
    for _, row in df.iterrows():
        company = row["Company Name"].strip()
        industry = row["Industry"].strip()
        symbol = row["Symbol"].strip()
        cat = row["type"]

        symbols.append({
            "name": symbol,
            "company": company,
            "industry": industry,
            "ticker": f"{symbol}.NS",
            "type": cat
        })
    return {"symbols": symbols}


# ============================================================
# 1️⃣ LOAD ALL 8 INDEX CONSTITUENTS
# ============================================================

# Large Cap
df_lc50     = load_index("Nifty50", "largecap_50")
df_lcnext50 = load_index("NiftyNext50", "largecap_100")

# Mid Cap
df_mc50     = load_index("NiftyMidcap50", "midcap_50")      # 101–150
df_mc100    = load_index("NiftyMidcap100", "midcap_100")    # 101–200
df_mc150    = load_index("NiftyMidcap150", "mid1cap_150")    # 101–250

# Small Cap
df_sc50     = load_index("NiftySmallcap50", "smallcap_50")    # 251–300
df_sc100    = load_index("NiftySmallcap100", "smallcap_100")  # 251–350
df_sc250    = load_index("NiftySmallcap250", "smallcap_250")  # 251–500


# ============================================================
# 2️⃣ BUILD UNIQUE LARGE CAP LIST (NO OVERLAP)
# ============================================================
df_largecap = pd.concat([df_lc50, df_lcnext50])
df_largecap.drop_duplicates(subset=["Symbol"], inplace=True)


# ============================================================
# 3️⃣ UNIQUE MIDCAP (REMOVE OVERLAP)
# ============================================================

# Remove overlap from mid100 (remove stocks already in mid50)
df_mc100_unique = df_mc100[~df_mc100["Symbol"].isin(df_mc50["Symbol"])]

# Remove overlap from mid150 (remove stocks from mid50+mid100)
df_mc150_unique = df_mc150[
    ~df_mc150["Symbol"].isin(df_mc50["Symbol"]) &
    ~df_mc150["Symbol"].isin(df_mc100["Symbol"])
]

df_midcap = pd.concat([df_mc50, df_mc100_unique, df_mc150_unique])
df_midcap.drop_duplicates(subset=["Symbol"], inplace=True)


# ============================================================
# 4️⃣ UNIQUE SMALLCAP (REMOVE OVERLAP)
# ============================================================

df_sc100_unique = df_sc100[~df_sc100["Symbol"].isin(df_sc50["Symbol"])]

df_sc250_unique = df_sc250[
    ~df_sc250["Symbol"].isin(df_sc50["Symbol"]) &
    ~df_sc250["Symbol"].isin(df_sc100["Symbol"])
]

df_smallcap = pd.concat([df_sc50, df_sc100_unique, df_sc250_unique])
df_smallcap.drop_duplicates(subset=["Symbol"], inplace=True)


# ============================================================
# 5️⃣ WRITE YAML FILES
# ============================================================

with open(os.path.join(OUTPUT_DIR, "largecap_50.yaml"), "w") as f:
    yaml.dump(df_to_yaml(df_lc50), f, sort_keys=False)

with open(os.path.join(OUTPUT_DIR, "largecap_100.yaml"), "w") as f:
    yaml.dump(df_to_yaml(df_lcnext50), f, sort_keys=False)

with open(os.path.join(OUTPUT_DIR, "midcap_50.yaml"), "w") as f:
    yaml.dump(df_to_yaml(df_mc50), f, sort_keys=False)

with open(os.path.join(OUTPUT_DIR, "midcap_100.yaml"), "w") as f:
    yaml.dump(df_to_yaml(df_mc100_unique), f, sort_keys=False)

with open(os.path.join(OUTPUT_DIR, "midcap_250.yaml"), "w") as f:
    yaml.dump(df_to_yaml(df_mc150_unique), f, sort_keys=False)

with open(os.path.join(OUTPUT_DIR, "smallcap_50.yaml"), "w") as f:
    yaml.dump(df_to_yaml(df_sc50), f, sort_keys=False)

with open(os.path.join(OUTPUT_DIR, "smallcap_100.yaml"), "w") as f:
    yaml.dump(df_to_yaml(df_sc100_unique), f, sort_keys=False)

with open(os.path.join(OUTPUT_DIR, "smallcap_250.yaml"), "w") as f:
    yaml.dump(df_to_yaml(df_sc250_unique), f, sort_keys=False)


print("\n🎉 Finished generating YAML files:")
print(" - largecap_50.yaml , largecap_100.yaml")
print(" - midcap_50.yaml , midcap_100.yaml , midcap_250.yaml")
print(" - smallcap_50.yaml , smallcap_100.yaml , smallcap_250.yaml\n")
