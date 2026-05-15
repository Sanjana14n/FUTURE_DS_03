import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
leads_df = pd.read_csv("dataset/olist_marketing_qualified_leads_dataset.csv")
deals_df = pd.read_csv("dataset/olist_closed_deals_dataset.csv")

# -----------------------------
# Total Leads and Closed Deals
# -----------------------------
total_leads = leads_df['mql_id'].count()
closed_deals = deals_df['mql_id'].count()

conversion_rate = (closed_deals / total_leads) * 100

print("Total Leads:", total_leads)
print("Closed Deals:", closed_deals)
print("Conversion Rate:", round(conversion_rate, 2), "%")

# -----------------------------
# 1. Funnel Analysis Chart
# -----------------------------
funnel_data = [total_leads, closed_deals]
funnel_labels = ['Total Leads', 'Closed Deals']

plt.figure(figsize=(6,4))
plt.bar(funnel_labels, funnel_data)
plt.title("Marketing Funnel Analysis")
plt.ylabel("Count")
plt.savefig("images/funnel_analysis.png")
plt.close()

# -----------------------------
# 2. Leads by Source
# -----------------------------
source_counts = leads_df['origin'].value_counts().head(5)

plt.figure(figsize=(8,5))
source_counts.plot(kind='bar')
plt.title("Top Lead Sources")
plt.ylabel("Lead Count")
plt.xticks(rotation=0)
plt.savefig("images/lead_sources.png")
plt.close()

# -----------------------------
# 3. Business Type Analysis
# -----------------------------
business_counts = deals_df['business_type'].value_counts()

plt.figure(figsize=(8,5))
business_counts.plot(kind='bar')
plt.title("Closed Deals by Business Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("images/business_type_analysis.png")
plt.close()

# -----------------------------
# 4. Landing Page Analysis
# -----------------------------
landing_counts = leads_df['landing_page_id'].value_counts().head(10)

plt.figure(figsize=(10,5))
landing_counts.plot(kind='bar')
plt.title("Top Landing Pages")
plt.ylabel("Lead Count")
plt.xticks(rotation=45)
plt.savefig("images/landing_page_analysis.png")
plt.close()

print("All charts generated successfully!")