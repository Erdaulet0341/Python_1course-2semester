"""
create or replace function get_number(name varchar)
returns TABLE(phone_number varchar) as
$$
begin
    return query
    select accounts.phone_number from accounts where accounts.first_name = name;
end;
$$
language plpgsql;
"""