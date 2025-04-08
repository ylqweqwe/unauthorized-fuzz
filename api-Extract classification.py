import re

js_vue_pattern = re.compile(r'(?:^|[/\s])([\w/-]+\.js(?:\?.*)?|[\w/-]+\.vue(?:\?.*)?)(?:\s|$)')
api_pattern = re.compile(r'/(?:api|rest|play|bi|crm|op)/[\w/-]+') 
domain_pattern = re.compile(r'(https?://[^\s]+)')


with open('js.txt', 'w', encoding='utf-8') as js_file, \
        open('api.txt', 'w', encoding='utf-8') as api_file, \
        open('domain.txt', 'w', encoding='utf-8') as domain_file, \
        open('*.txt', 'w', encoding='utf-8') as other_file:

    with open('1.txt', 'r', encoding='utf-8') as infile:
        for line in infile:

            js_matches = js_vue_pattern.findall(line)
            for match in js_matches:
                js_file.write(match.strip() + '\n')

            api_matches = api_pattern.findall(line)
            for match in api_matches:

                if not match.startswith('/'):
                    match = '/' + match
                api_file.write(match.strip() + '\n')


            domain_matches = domain_pattern.findall(line)
            for match in domain_matches:
                domain_file.write(match.strip() + '\n')

            remaining = line
            for pattern in [js_vue_pattern, api_pattern, domain_pattern]:
                remaining = pattern.sub('', remaining)


            if remaining.strip():
                other_file.write(remaining.strip() + '\n')
