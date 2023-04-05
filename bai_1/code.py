from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd



transactions = [
        ["a", "c", "d"],
        ["a", "c"],
        ["c", "e"],
        ["a", "b", "d", "e"],
        ["b", "d"],
        ["a", "b", "d", "e"]
    ]

te = TransactionEncoder()
te_ary = te.fit_transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_sets = apriori(df, min_support=0.3, use_colnames=True)
print("Frequent sets:")
print(frequent_sets)

rules = association_rules(frequent_sets, metric="confidence", min_threshold=1)
print("Rules:")
print(rules[['antecedents', 'consequents', 'confidence']])