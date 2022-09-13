import requests
from constants import DATA, ROOT
import yaml

OC_PATH = DATA.joinpath("organizing_committee.yml")
SPC_PATH = DATA.joinpath("program_committee.yml")
PROPS = {
    "P664": OC_PATH,
    "P5804": SPC_PATH,
}
#: Wikidata SPARQL endpoint. See https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service#Interfacing
WIKIDATA_ENDPOINT = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"

SPARQL = """\
SELECT 
  ?person ?personLabel ?personDescription ?genderLabel ?image
  ?nationalityLabel ?orcid ?linkedin ?twitter ?gscholar ?github
  (GROUP_CONCAT(DISTINCT ?topic_label; separator=", ") AS ?topics)
  (MAX(?start_date) as ?max_start_date)
  (SAMPLE(?employerLabel) as ?employerLabel_)
WHERE 
{
  wd:Q111430238 wdt:%s ?person .
  ?person wdt:P496 ?orcid .
  OPTIONAL { ?person wdt:P18 ?image . }
  OPTIONAL { ?person wdt:P21 ?gender . }
  OPTIONAL { ?person wdt:P2002 ?twitter . }
  OPTIONAL { ?person wdt:P27 ?nationality . }
  OPTIONAL { ?person wdt:P6634 ?linkedin . }
  OPTIONAL { ?person wdt:P1960 ?gscholar . }
  OPTIONAL { ?person wdt:P2037 ?github . }
  OPTIONAL { ?person wdt:P101 ?topic . ?topic rdfs:label ?topic_label . FILTER (LANG(?topic_label) = 'en') }
  OPTIONAL { 
    ?person p:P108 ?statement .
    ?statement ps:P108 ?employer .
    ?employer rdfs:label ?employerLabel
    filter(lang(?employerLabel) = "en")
    OPTIONAL { 
      ?statement pq:P580 ?start_date . 
    }
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # Helps get the label in your language, if not, then en language
}
GROUP BY
  ?person ?personLabel ?personDescription ?genderLabel ?image
  ?nationalityLabel ?orcid ?linkedin ?twitter ?gscholar ?github
ORDER BY ?personLabel
"""


def query_wikidata(sparql: str) -> list[dict[str, any]]:
    """Query Wikidata's sparql service.

    :param sparql: A SPARQL query string
    :return: A list of bindings
    """
    res = requests.get(WIKIDATA_ENDPOINT, params={"query": sparql, "format": "json"})
    res.raise_for_status()
    res_json = res.json()
    return res_json["results"]["bindings"]


def main():
    for prop, path in PROPS.items():
        results = query_wikidata(SPARQL % prop)
        rows = []
        for bindings in results:
            for url in ["person"]:
                if url in bindings:
                    bindings[url]["value"] = bindings[url]["value"].split("/")[-1]
            rows.append({key: value["value"] for key, value in bindings.items()})
        path.write_text(yaml.safe_dump(rows))


if __name__ == '__main__':
    main()
