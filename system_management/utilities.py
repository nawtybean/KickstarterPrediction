from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


def select_data(queryset, column_name):
    df = []
    try:
        for query in queryset:
            record = {
                'id': query['id'],
                'text': query[column_name]
            }
            df.append(record)
        if df and len(df) > 1:
            df = sorted(df, key=lambda item: item['text'], reverse=False)
    except:
        pass
    return df
