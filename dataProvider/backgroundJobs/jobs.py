from django.conf import settings
import pandas as pd

# Import library
from defillama import DefiLlama


# Client object to interact with DeFi Llama API
def get_defillama_data():
    print('in def...')
    llama = DefiLlama()
    try:
        data = llama.get_all_protocols()
        df = pd.DataFrame.from_records(data)
        temp = df[['name', 'symbol', 'mcap', 'tvl']].head(10)

    except Exception as e:
        temp = {'message': "can't get Defi-llama data",
                'error': e}
    # print(type(data))
    # print(len(data))
    print(temp)
