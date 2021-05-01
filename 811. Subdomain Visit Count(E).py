c = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

# class Solution:
#     def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
#         h = dict()
#         for i in cpdomains:
#             p = i.split(' ')
#             d = p[1]
#             h[d] = h.get(d,0) + int(p[0])
#             while d.find('.') != -1:
#                 d = d[d.find('.')+1:]
#                 h[d] = h.get(d,0) + int(p[0])
#         res = []
#         for i in h:
#             res.append(str(h[i])+' '+i)
#         return res

    # def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    #     h = defaultdict(int)
    #     for i in cpdomains:
    #         count = int(re.findall('[0-9]+',i)[0])
    #         domain = re.findall('[a-z]+',i)
    #         for i in range(len(domain)):
    #             h['.'.join(domain[i:])] += count
    #     return [f'{y} {x}' for x, y in h.items()]