FROM python:3.7.2

# maintainer of the image
LABEL maintainer="sboddu@ebi.ac.uk"
# Environment variable
ENV PYTHONUNBUFFERED TRUE

COPY . /usr/src/genome-search

WORKDIR /usr/src/genome-search

RUN pip3 install --no-cache-dir -r requirements.txt \
    && python dump_species.py --fetch_by_genome Homo_sapiens Triticum_aestivum Caenorhabditis_elegans Escherichia_coli_str_k_12_substr_mg1655 Saccharomyces_cerevisiae Plasmodium_falciparum \
    && echo 'y' | python dump_species.py --create_from_file /usr/src/genome-search/configs/grch37.json \
    && echo 'y' | python index_species.py

EXPOSE 8011

CMD ["gunicorn","--bind=0.0.0.0:8011","--workers=10","--preload","app:app"]

