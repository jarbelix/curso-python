# Install with 'pip install ms_active_directory'
from ms_active_directory import ADDomain


domain_dns_name = 'tiozaodolinux.com'
domain_servers = ['ldaps://auth.tiozaodolinux.com']
domain_user='Administrator@tiozaodolinux.com'
domain_password='SuperSecretPassword@2025'
domain_user_attrs=['cn', 'sn', 'title', 'description', 'physicalDeliveryOfficeName', 'telephoneNumber', 'givenName', 'displayName', 
                   'department', 'company', 'name', 'sAMAccountName', 'userPrincipalName', 'mail', 'loginShell', 'objectGUID', 'objectSid' ]
domain_group_attrs=['cn', 'sn', 'description', 'name', 'sAMAccountName', 'member', 'objectGUID', 'objectSid']

domain = ADDomain(domain_dns_name, ldap_servers_or_uris=domain_servers)
session = domain.create_session_as_user(user=domain_user, password=domain_password)

# # find_functional_level returns an enum indicating the level.
# # decision making based on level should be done based on the
# # needs of your application
# print(domain.find_functional_level())

# # might print "['EXTERNAL', 'DIGEST-MD5']"
# print(domain.find_supported_sasl_mechanisms())

# # returns a python datetime object in utc time
# curr_time = domain.find_current_time()

# # allowed drift defaults to 5 minutes which is the kerberos standard,
# # but we can use a shorter window to detect drift before it causes an
# # outage. this returns a boolean
# synced = domain.is_close_in_time_to_localhost(allowed_drift_seconds=60)

# # returns a map that maps server hostnames -> ip addresses, where
# # the hostnames are computers running dns services
# dns_map = session.find_dns_servers_for_domain()
# ip_addrs = dns_map.values()
# hostnames = dns_map.keys()
# print(f'DNS MAP = {dns_map}')
# print(f'IP ADDRS = {ip_addrs}')
# print(f'hostnames = {hostnames}')

# Find user by name
user = session.find_user_by_sam_name('tiozao', domain_user_attrs)

# Find group by name
group = session.find_group_by_sam_name('Turma da Monica', domain_group_attrs)

# users and groups support a generic "get" for any attributes queried
print()
print(f''.rjust(70,'='))
print(f'USER:'.ljust(10,'.'),f'{user.distinguished_name}')
print(f''.rjust(70,'='))
for attr in domain_user_attrs:
    if user.get(attr) != None:
        print(attr.ljust(30,'-'),' : ',user.get(attr))

print()
print(f''.rjust(70,'='))
print(f'GROUP:'.ljust(10,'.'),f'{group.distinguished_name}')
print(f''.rjust(70,'='))

for attr in domain_group_attrs:
    if group.get(attr) != None:
        print(attr.ljust(30,'-'),' : ',group.get(attr))
#        print(f'{attr}:\t\t{group.get(attr)}')
