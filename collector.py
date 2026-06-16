import pandas as pd
from datetime import datetime

from transaction_collector import collect_transactions


def unix_to_datetime(timestamp):

    return datetime.fromtimestamp(
        timestamp
    ).strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )[:-3]


print("Dang thu thap 100 giao dich...")

transactions = collect_transactions(
    max_records=100
)

rows = []

record_id = 1

for tx in transactions:

    try:

        value_eth = int(
            tx["value"],
            16
        ) / 10**18

        receipt = tx["receipt"]

        gas_used = int(
            receipt["gasUsed"],
            16
        )

        gas_price = int(
            receipt["effectiveGasPrice"],
            16
        )

        transaction_fee = (
            gas_used * gas_price
        ) / 10**18

        rows.append({

            "record_id":
                record_id,

            "tx_hash":
                tx["tx_hash"],

            "value_eth":
                value_eth,

            "gas_used":
                gas_used,

            "gas_price":
                gas_price,

            "transaction_fee":
                transaction_fee,

            "send_time":
                unix_to_datetime(
                    tx["send_time"]
                ),

            "receive_time":
                unix_to_datetime(
                    tx["receive_time"]
                ),

            "delay_ms":
                round(
                    tx["delay_ms"],
                    3
                ),

            "payload_size":
                tx["payload_size"],

            "request_status":
                tx["request_status"]

        })

        record_id += 1

    except Exception as e:

        print(
            "Bo qua giao dich:",
            e
        )

df = pd.DataFrame(rows)

df.to_csv(
    "Application_Data.csv",
    index=False
)

print(
    f"Da ghi {len(df)} dong vao Application_Data.csv"
)
