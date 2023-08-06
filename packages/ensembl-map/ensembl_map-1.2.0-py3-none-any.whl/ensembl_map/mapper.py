import logging

from .ensembl import Ensembl
from .convert import get_convert_func
from .features import get_load_function
from .symbol import get_transcripts
from .util import assert_valid_position


def cds_to_exon(feature, start, end=None, raise_error=True):
    """Map CDS coordinates to exon coordinates."""
    result = []
    for pos in cds_to_transcript(feature, start, end, raise_error=False):
        result.extend(transcript_to_exon(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map CDS {feature} to an exon")
    return result


def cds_to_gene(feature, start, end=None, raise_error=True):
    """Map CDS coordinates to gene coordinates."""
    result = []
    for pos in cds_to_transcript(feature, start, end, raise_error=False):
        result.extend(transcript_to_gene(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map CDS {feature} to a gene")
    return result


def cds_to_protein(feature, start, end=None, raise_error=True):
    """Map CDS coordinates to protein coordinates."""
    result = _map(feature, start, end, "cds", "protein")
    if not result and raise_error:
        raise ValueError(f"Could not map CDS {feature} to a protein")
    return result


def cds_to_transcript(feature, start, end=None, raise_error=True):
    """Map CDS coordinates to transcript coordinates."""
    result = _map(feature, start, end, "cds", "transcript")
    if not result and raise_error:
        raise ValueError(f"Could not map CDS {feature} to a transcript")
    return result


def contig_to_cds(contig, start, end=None, raise_error=True):
    """Map contig coordinates to transcript coordinates."""
    result = []
    for pos in contig_to_gene(contig, start, end, raise_error=False):
        result.extend(gene_to_cds(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map {contig, start, end} to a CDS")
    return result


def contig_to_gene(contig, start, end=None, raise_error=True):
    """Map contig coordinates to gene coordinates."""
    result = []

    if end is None:
        end = start

    for gene in Ensembl().data.genes_at_locus(contig, start, end):
        gstart = start if start >= gene.start else gene.start
        gend = end if end <= gene.end else gene.end
        result.extend(_map(gene.gene_id, gstart, gend, "gene", "gene"))

    if not result and raise_error:
        raise ValueError(f"Could not map {contig, start, end} to a gene")
    return result


def contig_to_protein(contig, start, end=None, raise_error=True):
    """Map contig coordinates to protein coordinates."""
    result = []
    for pos in contig_to_gene(contig, start, end, raise_error=False):
        result.extend(gene_to_protein(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map {contig, start, end} to a protein")
    return result


def contig_to_transcript(contig, start, end=None, raise_error=True):
    """Map contig coordinates to transcript coordinates."""
    result = []
    for pos in contig_to_gene(contig, start, end, raise_error=False):
        result.extend(gene_to_transcript(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map {contig, start, end} to a transcript")
    return result


def exon_to_cds(feature, raise_error=True):
    """Map an exon to CDS coordinates."""
    try:
        exon = Ensembl().data.exon_by_id(feature)
    except TypeError:
        logging.error(f"No exon '{feature}' found")
        return []

    result = _map(feature, exon.start, exon.end, "exon", "cds")
    if not result and raise_error:
        raise ValueError(f"Could not map exon {feature} to a CDS")
    return result


def exon_to_gene(feature, raise_error=True):
    """Map an exon to gene coordinates."""
    result = []
    for pos in exon_to_transcript(feature, raise_error=False):
        result.extend(transcript_to_gene(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map exon {feature} to a gene")
    return result


def exon_to_protein(feature, raise_error=True):
    """Map an exon to gene coordinates."""
    result = []
    for pos in exon_to_cds(feature, raise_error=False):
        result.extend(cds_to_protein(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map exon {feature} to a protein")
    return result


def exon_to_transcript(feature, raise_error=True):
    """Map an exon to transcript coordinates."""
    result = []

    try:
        exon = Ensembl().data.exon_by_id(feature)
    except TypeError:
        logging.error(f"No exon '{feature}' found")
        return result

    # Filter out transcripts that don't contain the query exon.
    valid_transcripts = [i.transcript_id for i in get_transcripts(feature, "exon")]
    for pos in gene_to_transcript(exon.gene_id, exon.start, exon.end, raise_error=False):
        if pos.transcript_id in valid_transcripts:
            result.append(pos)
        else:
            logging.debug(f"{pos.transcript_id} does not contain exon {exon.exon_id}")

    if not result and raise_error:
        raise ValueError(f"Could not map exon {feature} to a transcript")
    return result


def gene_to_cds(feature, start, end=None, raise_error=True):
    """Map gene coordinates to CDS coordinates."""
    result = []
    for pos in gene_to_transcript(feature, start, end, raise_error=False):
        result.extend(transcript_to_cds(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map gene {feature} to a CDS")
    return result


def gene_to_exon(feature, start, end=None, raise_error=True):
    """Map gene coordinates to exon coordinates."""
    result = _map(feature, start, end, "gene", "exon")
    if not result and raise_error:
        raise ValueError(f"Could not map gene {feature} to an exon")
    return result


def gene_to_protein(feature, start, end=None, raise_error=True):
    """Map gene coordinates to protein coordinates."""
    result = []
    for pos in gene_to_cds(feature, start, end, raise_error=False):
        result.extend(cds_to_protein(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map gene {feature} to a protein")
    return result


def gene_to_transcript(feature, start, end=None, raise_error=True):
    """Map gene coordinates to transcript coordinates."""
    result = _map(feature, start, end, "gene", "transcript")
    if not result and raise_error:
        raise ValueError(f"Could not map gene {feature} to a transcript")
    return result


def protein_to_cds(feature, start, end=None, raise_error=True):
    """Map protein coordinates to CDS coordinates."""
    result = _map(feature, start, end, "protein", "cds")
    if not result and raise_error:
        raise ValueError(f"Could not map protein {feature} to a CDS")
    return result


def protein_to_exon(feature, start, end=None, raise_error=True):
    """Map protein coordinates to exon coordinates."""
    result = []
    for pos in protein_to_transcript(feature, start, end, raise_error=False):
        result.extend(transcript_to_exon(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map protein {feature} to an exon")
    return result


def protein_to_gene(feature, start, end=None, raise_error=True):
    """Map protein coordinates to gene coordinates."""
    result = []
    for pos in protein_to_transcript(feature, start, end, raise_error=False):
        result.extend(transcript_to_gene(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map protein {feature} to a gene")
    return result


def protein_to_transcript(feature, start, end=None, raise_error=True):
    """Map protein coordinates to transcript coordinates."""
    result = []
    for pos in protein_to_cds(feature, start, end, raise_error=False):
        result.extend(cds_to_transcript(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map protein {feature} to a transcript")
    return result


def transcript_to_cds(feature, start, end=None, raise_error=True):
    """Map transcript coordinates to CDS coordinates."""
    result = _map(feature, start, end, "transcript", "cds")
    if not result and raise_error:
        raise ValueError(f"Could not map transcript {feature} to a CDS")
    return result


def transcript_to_exon(feature, start, end=None, raise_error=True):
    """Map transcript coordinates to exon coordinates."""
    result = []
    for pos in transcript_to_gene(feature, start, end, raise_error=False):
        result.extend(gene_to_exon(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map transcript {feature} to an exon")
    return result


def transcript_to_gene(feature, start, end=None, raise_error=True):
    """Map transcript coordinates to gene coordinates."""
    result = _map(feature, start, end, "transcript", "gene")
    if not result and raise_error:
        raise ValueError(f"Could not map transcript {feature} to a gene")
    return result


def transcript_to_protein(feature, start, end=None, raise_error=True):
    """Map transcript coordinates to protein coordinates."""
    result = []
    for pos in transcript_to_cds(feature, start, end, raise_error=False):
        result.extend(cds_to_protein(*pos.to_tuple(), raise_error=False))

    if not result and raise_error:
        raise ValueError(f"Could not map transcript {feature} to a protein")
    return result


def _map(feature, start, end, from_type, to_type):
    """
    Template function for mapping a feature to the associated transcript(s), then 
    converting the given coordinates.

    Args:
        feature (str): feature name or Ensembl ID
        start (int): first position relative to `feature`
        end (int or None): second position relative to `feature`
        from_type (str): coordinates relative to this type of feature (e.g. 'gene')
        to_type (str): map coordinates to this type of feature (e.g 'transcript')
        
    Returns:
        list: of converted coordinates, mapped to a `Feature` instance
    """
    result = []

    logging.debug(f"Mapping '{from_type}' ({feature}, {start}, {end}) to '{to_type}'")
    assert_valid_position(start, end)
    map_func = get_convert_func(from_type, to_type)
    load_func = get_load_function(to_type)

    for transcript in get_transcripts(feature, from_type):
        try:
            position = map_func(transcript, start, end)
            logging.debug(f"Position: {position}")
            feature_obj = load_func(transcript, *position)
            logging.debug(f"Parsed {transcript} at {position} to {feature_obj}")
            result.append(feature_obj)
        except ValueError as exc:
            logging.debug(exc)
            continue

    return result
