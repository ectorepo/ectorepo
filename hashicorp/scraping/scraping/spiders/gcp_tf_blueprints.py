import scrapy
import re
from urllib.parse import urlparse

# response.xpath
# .devsite-table-wrapper doesn't exist in raw source
# response.css('devsite-filter table td a').getall()
# response.css('devsite-filter table td a::attr(href)').getall()

# XmlItemExporter: https://docs.scrapy.org/en/latest/topics/feed-exports.html#xml
# Using Item Exporters: https://docs.scrapy.org/en/latest/topics/exporters.html

# two orgs: terraform-google-modules, GoogleCloudPlatform
# Github links all in the same format, same table, no pagination


class GcpTfBlueprintsSpider(scrapy.Spider):
    name = 'gcp_tf_blueprints'
    allowed_domains = ['cloud.google.com']
    start_urls = [
        'https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints'
    ]

    def parse(self, response):
        #repo_rows = response.css('devsite-filter table tr').getall()
        repo_links = response.css(
            'devsite-filter table td a::attr("href")').getall()

        for row in repo_links:
            repo_revision = "refs/heads/main"
            repo_remotes = "github"
            #repo_url = urllib.parse(row)
            # print(row)

            #repo_url = re.match('github.com/(.*)$', row).group(1)
            #org_name = repo_url.split('/')[1]
            #proj_name = repo_url.split('/')[2]
            #proj_name = row.re(f'https:///.*$')

            if row is None:
                pass
            else:
                rel_url = row.split('github.com/')[1]
                url_split = rel_url.split('/', 2)
                org_name = url_split[0]
                proj_name = url_split[1]
                yield {
                    "project": {
                        "name": f'{org_name}/{proj_name}',
                        "path": f'gcp/{proj_name}',
                        "revision": "refs/heads/main",
                        "remotes": "github"
                    }
                }

            # yield row

            # org_name = "GoogleCloudPlatform"
            # proj_name = "fdsa"
