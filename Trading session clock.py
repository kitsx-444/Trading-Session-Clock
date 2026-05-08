hour = int(input('Current hour: '))
pair = input('Pair: ').upper()
asia_pairs = ['USDJPY', 'AUDUSD', 'NZDUSD']
london_pairs = ['EURUSD', 'GBPUSD', 'EURGBP']
ny_pairs = ['EURUSD', 'GBPUSD', 'USDCAD']

asia = [0, 1, 2, 3, 4, 5, 6, 7, 8]
london = [8, 9, 10, 11, 12, 13, 14, 15, 16]
ny = [13, 14, 15, 16, 17, 18, 19, 20, 21]

print('---- Trading Session Clock ----')
print(f'UTC hour: {hour}')

if hour in asia:
	print('This is the Asian session.')
	if pair in asia_pairs:
		print(f'{pair} is favorable for that session.✅')
	else:
		print(f'{pair} is not favorable for that session.❎')

if hour in london and hour in ny:
	print('London/New York overlap!')

if hour in london:
	print('This is London session.')
	if pair in london_pairs:
		print(f'{pair} is favorable for that session.✅')
	else:
		print(f'{pair} is not favorable for that session.❎')

if hour in ny:
	print('This is New York session.')
	if pair in ny_pairs:
		print(f'{pair} is favorable for that session.✅')
	else:
		print(f'{pair} is not favorable for that session.❎')


