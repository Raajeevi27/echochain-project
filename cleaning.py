import pandas as pd

# =========================
# STEP 1: READ DATASET
# =========================
df = pd.read_csv("data/scraped_ebay_listings.csv")

# =========================
# STEP 2: BASIC INSPECTION
# =========================
print("First 5 rows:\n", df.head())

print("\nDataset Info:")
print(df.info())

# =========================
# STEP 3: CHECK ISSUES
# =========================
print("\nMissing Values:\n", df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nColumns:", df.columns)

# =========================
# STEP 4: CLEANING
# =========================

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# =========================
# STEP 5: CLEAN SPECIFIC COLUMNS
# =========================

# Clean price column
if 'price' in df.columns:
    df['price'] = df['price'].astype(str).str.replace(r'[₹$,]', '', regex=True)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Example: clean RAM column (if exists)
if 'ram' in df.columns:
    df['ram'] = df['ram'].astype(str).str.replace('GB', '')

# =========================
# STEP 6: FINAL CHECK
# =========================
print("\nAfter Cleaning:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

# =========================
# STEP 7: SAVE CLEAN DATA
# =========================
df.to_csv("data/cleaned_dataset.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")