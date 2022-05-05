"""
create or replace function get_numbe(name varchar)
returns TABLE(phone_number varchar) as
$$
begin
    return query
    select phonebook.phone_number from phonebook where phonebook.first_name = name;
end;
$$
language plpgsql;
"""