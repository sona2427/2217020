import csv

def shortenlink(long_link, max_val_time, keyword, current_time, used_keywords):
    base_url = "https://host2217020/"
    unique_keyword = keyword
    count = 1
    while unique_keyword in used_keywords:
        unique_keyword = f"{keyword}{count}"
        count += 1
    used_keywords.add(unique_keyword)
    final_link = f"{base_url}{unique_keyword}"
    hours, minutes = map(int, current_time.split(':'))
    final_minutes = (hours * 60 + minutes + int(max_val_time)) % 1440
    final_hours = final_minutes // 60
    final_minutes %= 60
    final_time = f"{final_hours:02}:{final_minutes:02}"
    return final_link, final_time, unique_keyword

input_file = 'data.csv'
rows = []
used_keywords = set()

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    for row in reader:
        long_link = row['link'].strip()
        max_val_time = row['max_val_time'].strip()
        keyword = row['keyword'].strip()
        current_time = row['current_time'].strip()
        final_link, final_time, unique_keyword = shortenlink(long_link, max_val_time, keyword, current_time, used_keywords)
        row['final_link'] = final_link
        row['final_time'] = final_time
        row['keyword'] = unique_keyword
        rows.append(row)

with open(input_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['link', 'max_val_time', 'keyword', 'current_time', 'final_link', 'final_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
