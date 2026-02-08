import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. 讀取與過濾資料 (限縮至你指定的四個特徵)
df = pd.read_csv('Access_to_Care_Dataset.csv')
target_topics = [
    'Delayed getting medical care due to cost among adults',
    'Did not get needed medical care due to cost',
    'Did not get needed mental health care due to cost',
    'Did not take medication as prescribed to save money'
]
filtered_df = df[df['TOPIC'].isin(target_topics)]

# 2. 進行 Pivot：每一行是一個群組，欄位是不同指標的平均估計值
# 我們排除 'Total' 群組，只看具體的細分群組
cluster_input = filtered_df.pivot_table(
    index='SUBGROUP', 
    columns='TOPIC', 
    values='ESTIMATE', 
    aggfunc='mean'
).dropna() # 確保參與分群的群組四個指標都有資料

# 3. 標準化資料 (Scaling)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(cluster_input)

# 4. 執行 K-Means 分群 (分為 3 群)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(scaled_features)

# 5. 合併結果並分析
cluster_input['Cluster'] = cluster_labels

# 定義風險等級 (計算每群的平均 estimate，越高代表風險越高)
cluster_risk = cluster_input.groupby('Cluster').mean().sum(axis=1).sort_values(ascending=False)
risk_mapping = {
    cluster_risk.index[0]: 'High Risk (Vulnerable)',
    cluster_risk.index[1]: 'Moderate Risk',
    cluster_risk.index[2]: 'Low Risk'
}
cluster_input['Risk_Level'] = cluster_input['Cluster'].map(risk_mapping)

# 6. 輸出高風險群體清單
high_risk_groups = cluster_input[cluster_input['Risk_Level'] == 'High Risk (Vulnerable)'].index.tolist()

print("分群分析完成！")
print(f"高風險群體數量: {len(high_risk_groups)}")
print("\n部分高風險群體範例:")
print(high_risk_groups[:10])

# 儲存結果
cluster_input.to_csv('Subgroup_Clustering_Analysis.csv')