def identify_whales(transactions, threshold=1000):
    whales = [tx for tx in transactions if tx['amount'] >= threshold]
    return whales

tx_list = [{'id': 1, 'amount': 50}, {'id': 2, 'amount': 1500}, {'id': 3, 'amount': 5000}]
print(f"Whale Transactions found: {identify_whales(tx_list)}")
