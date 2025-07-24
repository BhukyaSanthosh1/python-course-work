def count_messages(msgs):
    print("Total messages:", len(msgs))
def unique_users(msgs):
    users = []
    for m in msgs:
        name = m.split(":")[0]
        if name not in users:
            users.append(name)
    print("Unique users in the chat:", set(users))
def total_words(msgs):
    total = 0
    for m in msgs:
        parts = m.split(":")
        if len(parts) > 1:
            words = parts[1].strip().split()
            total += len(words)
    print("Total words in the chat:", total)
def average_words(msgs):
    total = 0
    for m in msgs:
        parts = m.split(":")
        if len(parts) > 1:
            total += len(parts[1].strip().split())
    print("Average words per message:", round(total / len(msgs), 2))
def longest_message(msgs):
    longest = ""
    for m in msgs:
        if len(m) > len(longest):
            longest = m
    print("Longest message:", longest)
def most_active_user(msgs):
    users = []
    for m in msgs:
        users.append(m.split(":")[0])
    active = ""
    max_count = 0
    for u in users:
        c = users.count(u)
        if c > max_count:
            max_count = c
            active = u
    print("Most active user:", active, "(", max_count, "messages)")
def user_message_count(msgs):
    name = input("Enter user name: ")
    count = 0
    for m in msgs:
        if m.startswith(name + ":"):
            count += 1
    print("Messages sent by", name + ":", count)
def frequent_word_by_user(msgs):
    name = input("Enter user name: ")
    words = []
    for m in msgs:
        if m.startswith(name + ":"):
            for w in m.split(":")[1].strip().split():
                words.append(w.lower())
    word = ""
    max_count = 0
    for w in words:
        c = words.count(w)
        if c > max_count:
            max_count = c
            word = w
    print("Most frequent word used by", name + ":", '"' + word + '"')
def first_last_message(msgs):
    name = input("Enter user name: ")
    user_msgs = []
    for m in msgs:
        if m.startswith(name + ":"):
            user_msgs.append(m)
    if user_msgs:
        print("First message by", name + ":", user_msgs[0])
        print("Last message by", name + ":", user_msgs[-1])
    else:
        print("No messages from", name)
def is_user_present(msgs):
    name = input("Enter user to check: ")
    found = False
    for m in msgs:
        if m.startswith(name + ":"):
            found = True
            break
    if found:
        print("User", name, "found in the chat.")
    else:
        print("User", name, "not found in the chat.")
def common_words(msgs):
    all_words = []
    repeat = []
    for m in msgs:
        parts = m.split(":")
        if len(parts) > 1:
            for w in parts[1].strip().split():
                w = w.lower()
                if w in all_words and w not in repeat:
                    repeat.append(w)
                else:
                    all_words.append(w)
    print("Common repeated words:", set(repeat))
def longest_avg_user(msgs):
    user_data = {}
    for m in msgs:
        parts = m.split(":")
        if len(parts) > 1:
            name = parts[0]
            wc = len(parts[1].strip().split())
            if name in user_data:
                user_data[name].append(wc)
            else:
                user_data[name] = [wc]
    max_avg = 0
    top_user = ""
    for u in user_data:
        avg = sum(user_data[u]) / len(user_data[u])
        if avg > max_avg:
            max_avg = avg
            top_user = u
    print("User with longest average message:", top_user, "(avg", round(max_avg, 2), "words)")
def mention_count(msgs):
    name = input("Enter name to search: ").lower()
    count = 0
    for m in msgs:
        if name in m.split(":")[1].lower():
            count += 1
    print("Messages mentioning", name + ":", count)
def remove_duplicates(msgs):
    unique = []
    for m in msgs:
        if m not in unique:
            unique.append(m)
    print("Unique messages count:", len(unique))
    for m in unique:
        print(m)
def sort_messages(msgs):
    sorted_msgs = sorted(msgs)
    for m in sorted_msgs:
        print(m)
def find_questions(msgs):
    for m in msgs:
        if "?" in m:
            print(m)
def reply_ratio(msgs):
    u1 = input("Enter user 1: ")
    u2 = input("Enter user 2: ")
    count = 0
    for m in msgs:
        if m.startswith(u2 + ":") and u1.lower() in m.lower():
            count += 1
    print("Reply ratio from", u2, "to", u1 + ":", count, "replies")
def deleted_msgs(msgs):
    count = 0
    for m in msgs:
        if m.endswith("This message was deleted"):
            count += 1
    print("Deleted messages found:", count)
n = int(input("Enter number of messages: "))
msgs = []
for i in range(n):
    msgs.append(input())
while True:
    print("\nMenu:")
    print("1. Total messages")
    print("2. Unique users")
    print("3. Total words")
    print("4. Average words")
    print("5. Longest message")
    print("6. Most active user")
    print("7. User message count")
    print("8. Frequent word by user")
    print("9. First & last message")
    print("10. Check user in chat")
    print("11. Repeated words")
    print("13. Longest average message user")
    print("14. Messages mentioning user")
    print("15. Remove duplicate messages")
    print("16. Sort messages")
    print("17. Extract questions")
    print("18. Reply ratio")
    print("19. Deleted messages")
    print("0. Exit")
    ch = input("Choose option: ")
    if ch == "1":
        count_messages(msgs)
    elif ch == "2":
        unique_users(msgs)
    elif ch == "3":
        total_words(msgs)
    elif ch == "4":
        average_words(msgs)
    elif ch == "5":
        longest_message(msgs)
    elif ch == "6":
        most_active_user(msgs)
    elif ch == "7":
        user_message_count(msgs)
    elif ch == "8":
        frequent_word_by_user(msgs)
    elif ch == "9":
        first_last_message(msgs)
    elif ch == "10":
        is_user_present(msgs)
    elif ch == "11":
        common_words(msgs)
    elif ch == "13":
        longest_avg_user(msgs)
    elif ch == "14":
        mention_count(msgs)
    elif ch == "15":
        remove_duplicates(msgs)
    elif ch == "16":
        sort_messages(msgs)
    elif ch == "17":
        find_questions(msgs)
    elif ch == "18":
        reply_ratio(msgs)
    elif ch == "19":
        deleted_msgs(msgs)
    elif ch == "0":
        break
    else:
        print("Invalid option")