import pytest
import json
from unittest.mock import patch, mock_open
from contact_man_sys import ContactManager


# Fixture to create a ContactManager instance with a test filename
@pytest.fixture
def contact_manager():
    return ContactManager("test_contacts.json")


# Fixture to provide sample contacts for testing
@pytest.fixture
def sample_contacts():
    return {
        "1": {
            "name": "John Doe",
            "phone": "0554333786",
            "email": "johndoe@gmail.com"
        },
        "2": {
            "name": "Kelvin Klein",
            "phone": "0553488789",
            "email": "kelvinklein@gmail.com"
        }
    }


# Test initialization of ContactManager
def test_init(contact_manager):
    assert contact_manager.filename == "test_contacts.json"
    assert isinstance(contact_manager.contacts, dict)
    assert contact_manager.next_index == 1


# Test loading contacts when file exists
def test_load_contacts_file_exists(contact_manager, sample_contacts):
    with patch("json.load", return_value=sample_contacts):
        with patch("os.path.exists", return_value=True):
            loaded_contacts = contact_manager.load_contacts()
    assert loaded_contacts == sample_contacts


# Test loading contacts when file does not exist
def test_load_contacts_file_not_exists(contact_manager):
    with patch("os.path.exists", return_value=False):
        loaded_contacts = contact_manager.load_contacts()
    assert loaded_contacts == {}


# Test saving contacts to a file
def test_save_contacts(contact_manager, sample_contacts):
    contact_manager.contacts = sample_contacts
    mock_file = mock_open()
    with patch("builtins.open", mock_file):
        contact_manager.save_contacts()
    handle = mock_file()
    written_content = ''.join(
        call.args[0] for call in handle.write.call_args_list
    )
    expected_content = json.dumps(sample_contacts, indent=2)
    assert written_content == expected_content


# Test adding a contact
@pytest.mark.parametrize("input_values, expected_output", [
    (
        ["John Doe", "0554333786", "johndoe@gmail.com"],
        "Contact 'John Doe' added successfully with index 1."
    ),
    (
        ["Kelvin Klein", "0553488789", "kelvinklein@gmail.com"],
        "Contact 'Kelvin Klein' added successfully with index 1."
    )
])
def test_add_contact(contact_manager, input_values, expected_output):
    with patch("builtins.input", side_effect=input_values):
        with patch("builtins.print") as mock_print:
            contact_manager.add_contact()
            mock_print.assert_called_with(expected_output)
    contact_index = str(contact_manager.next_index - 1)
    assert contact_manager.contacts[contact_index]["name"] == input_values[0]
    assert contact_manager.contacts[contact_index]["phone"] == input_values[1]
    assert contact_manager.contacts[contact_index]["email"] == input_values[2]


# Test viewing contacts when none exist
def test_view_contacts_empty(contact_manager, capsys):
    contact_manager.view_contacts()
    captured = capsys.readouterr()
    assert "No contacts found." in captured.out


# Test viewing contacts with pre-existing contacts
def test_view_contacts(contact_manager, sample_contacts, capsys):
    contact_manager.contacts = sample_contacts
    contact_manager.view_contacts()
    captured = capsys.readouterr()
    assert "John Doe" in captured.out
    assert "Kelvin Klein" in captured.out
    assert "0554333786" in captured.out
    assert "0553488789" in captured.out


# Test editing a contact
@pytest.mark.parametrize("index, new_values, expected_output", [
    (
        "1", ["New Name", "0550000000", "newname@example.com"],
        "Contact with index 1 updated successfully."
    ),
    (
        "1", ["", "0550000000", ""],
        "Contact with index 1 updated successfully."
    ),
    (
        "3", ["", "", ""],
        "Contact with index 3 not found."
    )
])
def test_edit_contact(
    contact_manager, sample_contacts,
    index, new_values, expected_output, capsys
):
    contact_manager.contacts = sample_contacts
    with patch("builtins.input", side_effect=[index] + new_values):
        contact_manager.edit_contact()
    captured = capsys.readouterr()
    assert expected_output in captured.out
    if index in sample_contacts:
        if new_values[0]:
            assert contact_manager.contacts[index]["name"] == new_values[0]
        if new_values[1]:
            assert contact_manager.contacts[index]["phone"] == new_values[1]
        if new_values[2]:
            assert contact_manager.contacts[index]["email"] == new_values[2]


# Test deleting a contact
@pytest.mark.parametrize("index, expected_output", [
    ("1", "Contact 'John Doe' with index 1 deleted successfully."),
    ("3", "Contact with index 3 not found.")
])
def test_delete_contact(
    contact_manager, sample_contacts, index, expected_output, capsys
):
    contact_manager.contacts = sample_contacts.copy()
    with patch("builtins.input", return_value=index):
        contact_manager.delete_contact()
    captured = capsys.readouterr()
    assert expected_output in captured.out
    if index in sample_contacts:
        assert index not in contact_manager.contacts
