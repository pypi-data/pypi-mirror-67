from typing import Dict, Iterable, List, Optional, Set, Tuple, NamedTuple, Union, Any
from collections import OrderedDict as odict
from itertools import chain

import torch
import warnings
import numpy as np
import gensim.downloader as api
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import fasttext
from gensim.test.utils import temporary_file

from flambe.compile.registrable import registrable_factory
from flambe.field import Field
from flambe.tokenizer import Tokenizer, WordTokenizer


def get_embeddings(
    embeddings: str,
    embeddings_format: str = 'glove',
    embeddings_binary: bool = False,
) -> KeyedVectors:
    """
    Get the embeddings model and matrix used in the setup function

    Parameters
    ----------
    embeddings : Optional[str], optional
        Path to pretrained embeddings, by default None
    embeddings_format : str, optional
        The format of the input embeddings, should be one of:
        'glove', 'word2vec', 'fasttext' or 'gensim'. The latter can
        be used to download embeddings hosted on gensim on the fly.
        See https://github.com/RaRe-Technologies/gensim-data
        for the list of available embedding aliases.
    embeddings_binary : bool, optional
        Whether the input embeddings are provided in binary format,
        by default False

    Returns
    -------
    KeyedVectors
        The embeddings object specified by the parameters.
    """
    model = None

    if embeddings_format == 'glove':
        with temporary_file('temp.txt') as temp:
            glove2word2vec(embeddings, temp)
            model = KeyedVectors.load_word2vec_format(temp, binary=embeddings_binary)
    elif embeddings_format == 'word2vec':
        model = KeyedVectors.load_word2vec_format(embeddings,
                                                  binary=embeddings_binary)
    elif embeddings_format == 'fasttext':
        model = fasttext.load_facebook_vectors(embeddings)
    elif embeddings_format == 'gensim':
        try:
            model = KeyedVectors.load(embeddings)
        except FileNotFoundError:
            model = api.load(embeddings)
    else:
        raise ValueError("Only formats supported are word2vec, fasttext and gensim")

    return model


class EmbeddingsInformation(NamedTuple):
    """
    Information about an embedding model.

    Parameters
    ----------
    embeddings : str
        Path to pretrained embeddings or the embedding name
        in case format is gensim.
    embeddings_format : str, optional
        The format of the input embeddings, should be one of:
        'glove', 'word2vec', 'fasttext' or 'gensim'. The latter can
        be used to download embeddings hosted on gensim on the fly.
        See https://github.com/RaRe-Technologies/gensim-data
        for the list of available embedding aliases.
    embeddings_binary : bool, optional
        Whether the input embeddings are provided in binary format,
        by default False.
    build_vocab_from_embeddings: bool
        Controls if all words from the optional provided
        embeddings will be added to the vocabulary and to the
        embedding matrix. Defaults to False.
    unk_init_all : bool, optional
        If True, every token not provided in the input embeddings is
        given a random embedding from a normal distribution.
        Otherwise, all of them map to the '<unk>' token.
    drop_unknown: bool
        Whether to drop tokens that don't have embeddings
        associated. Defaults to False.
        Important: this flag will only work when using embeddings.

    """
    embeddings: str
    embeddings_format: str = 'gensim'
    embeddings_binary: bool = False
    build_vocab_from_embeddings: bool = False
    unk_init_all: bool = False
    drop_unknown: bool = False


class TextField(Field):
    """Featurize raw text inputs

    This class performs tokenization and numericalization, as well as
    decorating the input sequences with optional start and end tokens.

    When a vocabulary is passed during initialiazation, it is used to
    map the the words to indices. However, the vocabulary can also be
    generated from input data, through the `setup` method. Once
    a vocabulary has been built, this object can also be used to load
    external pretrained embeddings.

    The pad, unk, sos and eos tokens, when given, are assigned the
    first indices in the vocabulary, in that order. This means, that
    whenever a pad token is specified, it will always use the 0 index.

    """

    def __init__(self,  # nosec
                 tokenizer: Optional[Tokenizer] = None,
                 lower: bool = False,
                 pad_token: Optional[str] = '<pad>',
                 unk_token: str = '<unk>',
                 sos_token: Optional[str] = None,
                 eos_token: Optional[str] = None,
                 embeddings_info: Optional[EmbeddingsInformation] = None,
                 embeddings: Optional[str] = None,
                 embeddings_format: str = 'glove',
                 embeddings_binary: bool = False,
                 unk_init_all: bool = False,
                 drop_unknown: bool = False,
                 max_seq_len: Optional[int] = None,
                 truncate_end: bool = False,
                 setup_all_embeddings: bool = False,
                 additional_special_tokens: Optional[List[str]] = None,
                 vocabulary: Optional[Union[Iterable[str], str]] = None) -> None:
        """Initialize the TextField.

        Parameters
        ----------
        tokenizer : Tokenizer, optional
            Tokenizer to use, by default WordTokenizer()
        lower : bool, optional
            If given, lowercase the input, by default False
        pad_token : str, optional
            Reserved padding token. Note that this object does not
            perform padding. Padding is done on the fly, when sampling.
            (defaults to '<pad>')
        unk_token : str, optional
            The token to use for out of vocabulary tokens
            (defaults to '<unk>')
        sos_token : str, optional
            Start of sentence tokens to add to the start of
            each sequence (defaults to '<sos>')
        eos : Iterable[str], optional
            List of end of sentence tokens to add to the end of each
            sequence (defaults to an empty list)
        embeddings_info : EmbeddingsInformation, optional
            The embeddings information. By default None
        embeddings : str
            WIlL BE DEPRECATED SOON. USE 'from_embeddings'
            FACTORY INSTEAD.
            Path to pretrained embeddings or the embedding name
            in case format is gensim.
        embeddings_format : str, optional
            WIlL BE DEPRECATED SOON. USE 'from_embeddings'
            FACTORY INSTEAD.
            The format of the input embeddings, should be one of:
            'glove', 'word2vec', 'fasttext' or 'gensim'. The latter can
            be used to download embeddings hosted on gensim on the fly.
            See https://github.com/RaRe-Technologies/gensim-data
            for the list of available embedding aliases.
        embeddings_binary : bool, optional
            WIlL BE DEPRECATED SOON. USE 'from_embeddings'
            FACTORY INSTEAD.
            Whether the input embeddings are provided in binary format,
            by default False
        unk_init_all : bool, optional
            If True, every token not provided in the input embeddings is
            given a random embedding from a normal distribution.
            Otherwise, all of them map to the '<unk>' token.
        drop_unknown: bool
            WIlL BE DEPRECATED SOON. USE 'from_embeddings'
            FACTORY INSTEAD.
            Whether to drop tokens that don't have embeddings
            associated. Defaults to False.
            Important: this flag will only work when using embeddings.
        max_seq_len: int, optional
            The maximum length possibly output by the process func.
            If len of input tokens is larger than this number - then
            the output will be truncated as a post processing step.
        truncate_end: bool
            Determines the window of observed text in process if the
            input is larger than max_seq_len. If this value is True
            the window starts from the end of the utterance.
            Defaults to False.
            example: max_seq_len=3, input_text=1 2 3 4 5
            truncate_end=false: output=1 2 3
            truncate_end=true: output=3 4 5
        setup_all_embeddings: bool
            WIlL BE DEPRECATED SOON. USE 'from_embeddings'
            FACTORY INSTEAD.
            Controls if all words from the optional provided
            embeddings will be added to the vocabulary and to the
            embedding matrix. Defaults to False.
        additional_special_tokens: Optional[List[str]]
            Additional special tokens beyond the pad, unk, eos and sos
            tokens.
        vocabulary: Union[List[str], str], optional
            Can be either a list of tokens or a file with a token on
            each line. If given, one can choose to allow expandion of
            the vocabulary or to freeze it.

        """
        if embeddings:
            if embeddings_info:
                raise ValueError(
                    "Cannot submit embeddings information and use the embeddings parameters" +
                    "simultaneously. Use the 'from_embeddings' factory instead.")

            warnings.warn("The embeddings-exclusive parameters " +
                          "('embeddings', 'embeddings_format', 'embeddings_binary', " +
                          "'setup_all_embeddings', 'drop_unknown', 'unk_init_all') " +
                          "will be deprecated in a future release. " +
                          "Please migrate to use the 'from_embeddings' factory.")

            embeddings_info = EmbeddingsInformation(
                embeddings=embeddings,
                embeddings_format=embeddings_format,
                embeddings_binary=embeddings_binary,
                build_vocab_from_embeddings=setup_all_embeddings,
                unk_init_all=unk_init_all,
                drop_unknown=drop_unknown
            )

        self.tokenizer = tokenizer or WordTokenizer()
        self.lower = lower

        self.pad = pad_token
        self.unk = unk_token
        self.sos = sos_token
        self.eos = eos_token

        self.embeddings_info = embeddings_info

        self.embedding_matrix: Optional[torch.Tensor] = None

        self.max_seq_len = max_seq_len
        self.truncate_end = truncate_end

        self.unk_numericals: Set[int] = set()

        # Load vocabulary if given
        if vocabulary is None:
            self.vocab: Dict = odict()
        elif isinstance(vocabulary, str):
            with open(vocabulary, 'r') as f:
                self.vocab = odict((tok, i) for i, tok in enumerate(f.read().splitlines()))
        elif isinstance(vocabulary, Iterable):
            self.vocab = odict((tok, i) for i, tok in enumerate(vocabulary))

        additional_special_tokens = additional_special_tokens or []
        specials = [pad_token, unk_token, sos_token, eos_token, *additional_special_tokens]
        self.specials = [special for special in specials if special is not None]
        self.register_attrs('vocab')

    @property
    def vocab_list(self) -> List[str]:
        """Get the list of tokens in the vocabulary.

        Returns
        -------
        List[str]
            The list of tokens in the vocabulary, ordered.

        """
        return list(self.vocab.keys())

    @property
    def vocab_size(self) -> int:
        """Get the vocabulary length.

        Returns
        -------
        int
            The length of the vocabulary

        """
        unique_ids = set(v for k, v in self.vocab.items())
        return len(unique_ids)

    def _flatten_to_str(self, data_sample: Union[List, Tuple, Dict]) -> str:
        """Converts any nested data sample to a str

        Used to build vocabs from complex file structures

        Parameters
        ----------
        data_sample: Union[List, Tuple, Dict]

        Returns
        -------
        str
            the flattened version, for vocab building

        """
        if isinstance(data_sample, list) or isinstance(data_sample, tuple):
            return ' '.join(self._flatten_to_str(s) for s in data_sample)
        elif isinstance(data_sample, dict):
            return ' '.join(self._flatten_to_str(s) for s in data_sample.values())
        elif isinstance(data_sample, str):
            return data_sample
        else:
            raise ValueError(f'Cannot process type {type(data_sample)} for vocab building.')

    def _build_vocab(self, *data: np.ndarray) -> None:
        """
        Build the vocabulary for this object based on the special
        tokens and the data provided.

        This method is safe to be called multiple times.

        Parameters
        ----------
        *data: np.ndarray
            The data

        """
        examples: Iterable = (e for dataset in data for e in dataset if dataset is not None)

        index = len(self.vocab) - 1

        # First load special tokens
        for token in self.specials:
            if token not in self.vocab:
                self.vocab[token] = index = index + 1

        for example in examples:
            example = self._flatten_to_str(example)
            # Lowercase if requested
            example = example.lower() if self.lower else example
            # Tokenize and add to vocabulary
            for token in self.tokenizer(example):
                if token not in self.vocab:
                    self.vocab[token] = index = index + 1

    def _build_embeddings(self, model: KeyedVectors,
                          setup_vocab_from_embeddings: bool,
                          initialize_unknowns: bool) -> Tuple[odict, torch.Tensor]:
        """
        Create the embeddings matrix and the new vocabulary in
        case this objects needs to use an embedding model.

        A new vocabulary needs to be built because of the parameters
        that could allow, for example, collapsing OOVs.

        Parameters
        ----------
        model: KeyedVectors
            The embeddings
        setup_vocab_from_embeddings: bool
            Controls if all words from the optional provided
            embeddings will be added to the vocabulary and to the
            embedding matrix. Defaults to False.
        initialize_unknowns
            If True, every unknown token will be assigned
            a random embedding from a normal distribution.
            Otherwise, all of them map to the '<unk>' token.

        Returns
        -------
        Tuple[OrderedDict, torch.Tensor]
            A tuple with the new embeddings and the embedding matrix
        """
        embedding_matrix: List[torch.Tensor] = []
        new_vocab: odict[str, int] = odict()

        new_index = -1

        tokens: Iterable[str] = self.vocab.keys()

        if setup_vocab_from_embeddings:
            tokens = chain(tokens, model.vocab.keys())

        for token in tokens:
            if token not in new_vocab:
                if token in model:
                    embedding_matrix.append(torch.tensor(model[token]))
                    new_vocab[token] = new_index = new_index + 1
                elif token in self.specials:
                    embedding_matrix.append(torch.randn(model.vector_size))
                    new_vocab[token] = new_index = new_index + 1
                else:
                    self.unk_numericals.add(self.vocab[token])

                    if initialize_unknowns:
                        embedding_matrix.append(torch.randn(model.vector_size))
                        new_vocab[token] = new_index = new_index + 1
                    else:
                        # Collapse all OOV's to the same <unk> token id
                        new_vocab[token] = new_vocab[self.unk]

        return new_vocab, torch.stack(embedding_matrix)

    def setup(self, *data: np.ndarray) -> None:
        """Build the vocabulary and sets embeddings.

        Parameters
        ----------
        data : Iterable[str]
            List of input strings.

        """
        self._build_vocab(*data)

        if self.embeddings_info:
            model = get_embeddings(self.embeddings_info.embeddings,
                                   self.embeddings_info.embeddings_format,
                                   self.embeddings_info.embeddings_binary)
            self.vocab, self.embedding_matrix = self._build_embeddings(
                model,
                self.embeddings_info.build_vocab_from_embeddings,
                self.embeddings_info.unk_init_all)

    # TODO update when we add generics
    def process(self, example:  # type: ignore
                Union[str, Tuple[Any], List[Any], Dict[Any, Any]]) \
            -> Union[torch.Tensor, Tuple[torch.Tensor, ...],
                     List[torch.Tensor], Dict[str, torch.Tensor]]:
        """Process an example, and create a Tensor.

        Parameters
        ----------
        example: str
            The example to process, as a single string

        Returns
        -------
        torch.Tensor
            The processed example, tokenized and numericalized

        """
        # special case of list of examples:
        if isinstance(example, list) or isinstance(example, tuple):
            return [self.process(e) for e in example]  # type: ignore
        elif isinstance(example, dict):
            return dict([(key, self.process(val)) for key, val in example.items()])  # type: ignore

        # Lowercase and tokenize
        example = example.lower() if self.lower else example
        tokens = self.tokenizer(example)

        # Add extra tokens
        if self.sos is not None:
            tokens = [self.sos] + list(tokens)
        if self.eos is not None:
            tokens = list(tokens) + [self.eos]

        # Numericalize
        numericals = []
        for token in tokens:
            if token not in self.vocab:
                if self.unk is None or self.unk not in self.vocab:
                    raise ValueError("Encounterd out-of-vocabulary token \
                                      but the unk_token is either missing \
                                      or not defined in the vocabulary.")
                else:
                    token = self.unk

            numerical = self.vocab[token]  # type: ignore

            if self.embeddings_info is not None and self.embeddings_info.drop_unknown and \
                    numerical in self.unk_numericals:
                # Don't add unknown tokens in case the flag is activated
                continue

            numericals.append(numerical)

        ret = torch.tensor(numericals).long()

        if self.max_seq_len is not None:
            if self.truncate_end:
                ret = ret[-self.max_seq_len:]
            else:
                ret = ret[:self.max_seq_len]
        return ret

    @registrable_factory
    @classmethod
    def from_embeddings(
        cls,
        embeddings: str,
        embeddings_format: str = 'glove',
        embeddings_binary: bool = False,
        build_vocab_from_embeddings: bool = False,
        unk_init_all: bool = False,
        drop_unknown: bool = False,
        additional_special_tokens: Optional[List[str]] = None,
        **kwargs,
    ):
        """
        Optional constructor to create TextField from embeddings params.

        Parameters
        ----------
        embeddings : Optional[str], optional
            Path to pretrained embeddings, by default None
        embeddings_format : str, optional
            The format of the input embeddings, should be one of:
            'glove', 'word2vec', 'fasttext' or 'gensim'. The latter can
            be used to download embeddings hosted on gensim on the fly.
            See https://github.com/RaRe-Technologies/gensim-data
            for the list of available embedding aliases.
        embeddings_binary : bool, optional
            Whether the input embeddings are provided in binary format,
            by default False
        build_vocab_from_embeddings: bool
            Controls if all words from the optional provided
            embeddings will be added to the vocabulary and to the
            embedding matrix. Defaults to False.
        unk_init_all : bool, optional
            If True, every token not provided in the input embeddings is
            given a random embedding from a normal distribution.
            Otherwise, all of them map to the '<unk>' token.
        drop_unknown: bool
            Whether to drop tokens that don't have embeddings
            associated. Defaults to False.
            Important: this flag will only work when using embeddings.
        additional_special_tokens: Optional[List[str]]
            Additional tokens that have a reserved interpretation in
            the context of the current experiment, and that should
            therefore never be treated as "unknown".
            Passing them in here will make sure that they will have
            their own embedding that can be trained.

        Returns
        -------
        TextField
            The constructed text field with the requested model.
        """
        embeddings_info = EmbeddingsInformation(
            embeddings=embeddings,
            embeddings_format=embeddings_format,
            embeddings_binary=embeddings_binary,
            build_vocab_from_embeddings=build_vocab_from_embeddings,
            unk_init_all=unk_init_all,
            drop_unknown=drop_unknown
        )

        return cls(
            embeddings_info=embeddings_info,
            additional_special_tokens=additional_special_tokens,
            **kwargs,
        )
