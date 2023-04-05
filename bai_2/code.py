# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori, association_rules
# import pandas as pd
#
# # CSDL giao dịch
# # transactions = [
# #         ["A", "B", "C"],
# #         ["A", "B"],
# #         ["A", "D", "E"],
# #         ["E", "D"],
# #         ["E", "C"],
# #         ["A", "D", "E"]
# #
# #     ]
#
# transactions = [
#         ["A", "B", "C"],
#         ["A", "B"],
#         ["A", "D","E"],
#         ["E", "D"],
#         ["E", "C"],
#         ["A", "D", "E"]
#     ]
#
# # Áp dụng thuật toán apriori để tìm tập phổ biến
# te = TransactionEncoder()
# te_ary = te.fit_transform(transactions)
# df = pd.DataFrame(te_ary, columns=te.columns_)
# frequent_sets = apriori(df, min_support=0.3, use_colnames=True)
# print("Frequent sets:")
# print(frequent_sets)
#
# # Tìm các luật kết hợp từ tập phổ biến
# rules = association_rules(frequent_sets, metric="confidence", min_threshold=1)
# print("Rules:")
# print(rules[['antecedents', 'consequents', 'confidence']])

from itertools import combinations


def get_frequent_itemsets(data, minsupp):
        # Tính độ hỗ trợ tối thiểu dựa trên tổng số giao dịch và ngưỡng minsupp
        minsupp_count = len(data) * minsupp

        # Tạo danh sách tất cả các mục và tập hạng mục
        all_items = sorted(list(set(item for transaction in data for item in transaction)))
        itemsets = [[item] for item in all_items]

        # Tìm các tập phổ biến bằng thuật toán Apriori
        frequent_itemsets = []
        k = 1
        while itemsets:
                # Tính hỗ trợ cho từng tập hạng mục
                itemsets_counts = {frozenset(itemset): 0 for itemset in itemsets}
                for transaction in data:
                        for itemset in itemsets_counts.keys():
                                if itemset.issubset(transaction):
                                        itemsets_counts[itemset] += 1

                # Lọc ra các tập phổ biến
                frequent_itemsets.extend(
                        [list(itemset) for itemset, count in itemsets_counts.items() if count >= minsupp_count])

                # Tạo các tập hạng mục mới kết hợp từ các tập hạng mục hiện tại
                itemsets = []
                for i, itemset in enumerate(sorted(itemsets_counts.keys())):
                        for j in range(i + 1, len(itemsets_counts)):
                                other_itemset = sorted(list(itemsets_counts.keys())[j])
                                new_itemset = sorted(list(itemset.union(other_itemset)))
                                if len(new_itemset) == k + 1 and new_itemset not in itemsets:
                                        itemsets.append(new_itemset)
                k += 1

        return frequent_itemsets

data = {
    'T1': ['A', 'B', 'C'],
    'T2': ['A', 'B'],
    'T3': ['A', 'D', 'E'],
    'T4': ['E', 'D'],
    'T5': ['E', 'C'],
    'T6': ['A', 'D', 'E'],
}

minsupp = 0.3

frequent_itemsets = get_frequent_itemsets(list(data.values()), minsupp)

print(frequent_itemsets)