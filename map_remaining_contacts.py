def get_dialog_ids(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    dialog_ids = [int(line.split(': ')[1]) for line in lines if line.startswith("ID: ")]
    return dialog_ids

def get_contacts(file_path):
    contacts = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith("ID: "):
            parts = line.strip().split(',')
            contact = {
                'id': int(parts[0].split(': ')[1]),
                'first_name': parts[1].split(': ')[1] if len(parts) > 1 and ': ' in parts[1] else '',
                'last_name': parts[2].split(': ')[1] if len(parts) > 2 and ': ' in parts[2] else '',
                'username': parts[3].split(': ')[1] if len(parts) > 3 and ': ' in parts[3] else '',
                'phone': parts[4].split(': ')[1] if len(parts) > 4 and ': ' in parts[4] else ''
            }
            contacts.append(contact)
    return contacts

def map_remaining_contacts(failed_ids, contacts):
    remaining_contacts = [contact for contact in contacts if contact['id'] in failed_ids]
    return remaining_contacts

def write_remaining_contacts(file_path, contacts):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('Remaining Contacts:\n')
        for contact in contacts:
            file.write(f"ID: {contact['id']}, First Name: {contact['first_name']}, Last Name: {contact['last_name']}, Username: {contact['username']}, Phone: {contact['phone']}\n")

if __name__ == "__main__":
    failed_dialog_ids = get_dialog_ids('failed_contacts.txt')
    all_contacts = get_contacts('contacts.txt')
    remaining_contacts = map_remaining_contacts(failed_dialog_ids, all_contacts)
    write_remaining_contacts('remaining.txt', remaining_contacts)
