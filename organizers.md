---
layout: default
title: Organizers
permalink: /organizers
---

## Organizing Committee

<dl>
{% for person in site.data.organizing_committee %}
<dt>
    <strong>{{ person.personLabel }}{% if person.note %} ({{ person.note }}){% endif %}</strong>
</dt>
<dd>
    <a href="https://bioregistry.io/orcid:{{ person.orcid }}">
        <img alt="ORCiD logo" src="img/icons/orcid.svg" style="max-height: 1rem; vertical-align: center;">
        {{ person.orcid }}
    </a>
    {% if person.twitter %}
    <a href="https://twitter.com/{{ person.twitter }}" style="margin: 0 0.5rem;">
        <img alt="Twitter logo" src="img/icons/twitter.svg" style="max-height: 1rem; vertical-align: center;">
        @{{ person.twitter }}
    </a>
    {% endif %}
    <a href="https://bioregistry.io/wikidata:{{ person.person }}" style="margin: 0 0.5rem;">
        <img alt="Wikidata logo" src="img/icons/wikidata.svg" style="max-height: 1rem; vertical-align: center;">
        {{ person.person }}
    </a>
    <p>{{ person.employerLabel_ }}</p>
</dd>
{% endfor %}
</dl>

## Scientific Program Committee

<dl>
{% for person in site.data.program_committee %}
<dt>
    <strong>{{ person.personLabel }}{% if person.note %} ({{ person.note }}){% endif %}</strong>
</dt>
<dd>
    <a href="https://bioregistry.io/orcid:{{ person.orcid }}">
        <img alt="ORCiD logo" src="img/icons/orcid.svg" style="max-height: 1rem; vertical-align: center;">
        {{ person.orcid }}
    </a>
    {% if person.twitter %}
    <a href="https://twitter.com/{{ person.twitter }}" style="margin: 0 0.5rem;">
        <img alt="Twitter logo" src="img/icons/twitter.svg" style="max-height: 1rem; vertical-align: center;">
        @{{ person.twitter }}
    </a>
    {% endif %}
    <a href="https://bioregistry.io/wikidata:{{ person.person }}" style="margin: 0 0.5rem;">
        <img alt="Wikidata logo" src="img/icons/wikidata.svg" style="max-height: 1rem; vertical-align: center;">
        {{ person.person }}
    </a>
    <p>{{ person.employerLabel_ }}</p>
</dd>
{% endfor %}
</dl>

## Travel Fellowship Committee

See [here](https://www.biocuration.org/travel-fellowship/) for more information about how to apply for a travel
fellowship.

<dl>
{% for person in site.data.travel_committee %}
<dt>
    <strong>{{ person.name }}{% if person.note %} ({{ person.note }}){% endif %}</strong>
</dt>
<dd>
    <a href="https://bioregistry.io/orcid:{{ person.orcid }}">
        <img alt="ORCiD logo" src="img/icons/orcid.svg" style="max-height: 1rem; vertical-align: center;">
        {{ person.orcid }}
    </a>
    {% if person.twitter %}
    <a href="https://twitter.com/{{ person.twitter }}" style="margin: 0 0.5rem;">
        <img alt="Twitter logo" src="img/icons/twitter.svg" style="max-height: 1rem; vertical-align: center;">
        @{{ person.twitter }}
    </a>
    {% endif %}
    <a href="https://bioregistry.io/wikidata:{{ person.person }}" style="margin: 0 0.5rem;">
        <img alt="Wikidata logo" src="img/icons/wikidata.svg" style="max-height: 1rem; vertical-align: center;">
        {{ person.person }}
    </a>
    <p>{{ person.employerLabel_ }}</p>
</dd>
{% endfor %}
</dl>
