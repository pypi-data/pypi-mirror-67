# coding: utf-8
from __future__ import unicode_literals

import io
import json
import pytest
import os
import shutil
import operator
from jsondiff import diff
import pandas as pd
from dframcy.trainer import (
    DframeConverter,
    DframeTrainer,
    DframeEvaluator,
    DframeTrainClassifier,
)


@pytest.mark.parametrize(
    "input_csv_file, output_json_file",
    [("data/training_data_format.csv", "data/training_data_converted.json")],
)
def test_cli_format_converter_full_pipeline(input_csv_file, output_json_file):
    dframe_converter = DframeConverter(
        train_path=input_csv_file, dev_path=input_csv_file
    )
    json_formatted_file_path, pipeline = dframe_converter.convert(
        input_csv_file, dframe_converter._nlp
    )

    with io.open(json_formatted_file_path, "r") as format_file:
        json_formatted_training_data = json.load(format_file)
    os.remove(json_formatted_file_path)

    with io.open(output_json_file, "r") as output_file:
        actual_json_formatted_training_data = json.load(output_file)

    assert diff(json_formatted_training_data, actual_json_formatted_training_data) == {}


@pytest.mark.parametrize("input_csv_file", ["data/training_data_format.csv"])
def test_cli_format_converter_only_tagger(input_csv_file):
    dframe_converter = DframeConverter(
        train_path=input_csv_file, dev_path=input_csv_file, pipeline="tagger"
    )
    json_formatted_file_path, pipeline = dframe_converter.convert(
        input_csv_file, dframe_converter._nlp
    )

    training_data_only_tagger = [
        {
            "id": 0,
            "paragraphs": [
                {
                    "raw": "Uber blew through $1 million a week",
                    "sentences": [
                        {
                            "tokens": [
                                {"id": 0, "orth": "Uber", "tag": "NNP"},
                                {"id": 1, "orth": "blew", "tag": "VBD"},
                                {"id": 2, "orth": "through", "tag": "IN"},
                                {"id": 3, "orth": "$", "tag": "$"},
                                {"id": 4, "orth": "1", "tag": "CD"},
                                {"id": 5, "orth": "million", "tag": "CD"},
                                {"id": 6, "orth": "a", "tag": "DT"},
                                {"id": 7, "orth": "week", "tag": "NN"},
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 1,
            "paragraphs": [
                {
                    "raw": "Android Pay expands to Canada",
                    "sentences": [
                        {
                            "tokens": [
                                {"id": 0, "orth": "Android", "tag": "NNP"},
                                {"id": 1, "orth": "Pay", "tag": "NNP"},
                                {"id": 2, "orth": "expands", "tag": "VBZ"},
                                {"id": 3, "orth": "to", "tag": "IN"},
                                {"id": 4, "orth": "Canada", "tag": "NNP"},
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 2,
            "paragraphs": [
                {
                    "raw": "Spotify steps up Asia expansion",
                    "sentences": [
                        {
                            "tokens": [
                                {"id": 0, "orth": "Spotify", "tag": "VB"},
                                {"id": 1, "orth": "steps", "tag": "VBZ"},
                                {"id": 2, "orth": "up", "tag": "RP"},
                                {"id": 3, "orth": "Asia", "tag": "NNP"},
                                {"id": 4, "orth": "expansion", "tag": "NN"},
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 3,
            "paragraphs": [
                {
                    "raw": "Google Maps launches location sharing",
                    "sentences": [
                        {
                            "tokens": [
                                {"id": 0, "orth": "Google", "tag": "NNP"},
                                {"id": 1, "orth": "Maps", "tag": "NNPS"},
                                {"id": 2, "orth": "launches", "tag": "VBZ"},
                                {"id": 3, "orth": "location", "tag": "NN"},
                                {"id": 4, "orth": "sharing", "tag": "NN"},
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 4,
            "paragraphs": [
                {
                    "raw": "Google rebrands its business apps",
                    "sentences": [
                        {
                            "tokens": [
                                {"id": 0, "orth": "Google", "tag": "NNP"},
                                {"id": 1, "orth": "rebrands", "tag": "VBZ"},
                                {"id": 2, "orth": "its", "tag": "PRP$"},
                                {"id": 3, "orth": "business", "tag": "NN"},
                                {"id": 4, "orth": "apps", "tag": "NNS"},
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 5,
            "paragraphs": [
                {
                    "raw": "look what i found on google! Joy",
                    "sentences": [
                        {
                            "tokens": [
                                {"id": 0, "orth": "look", "tag": "VB"},
                                {"id": 1, "orth": "what", "tag": "WP"},
                                {"id": 2, "orth": "i", "tag": "PRP"},
                                {"id": 3, "orth": "found", "tag": "VBD"},
                                {"id": 4, "orth": "on", "tag": "IN"},
                                {"id": 5, "orth": "google", "tag": "NNP"},
                                {"id": 6, "orth": "!", "tag": "."},
                            ]
                        },
                        {"tokens": [{"id": 0, "orth": "look", "tag": "VB"}]},
                    ],
                }
            ],
        },
    ]

    with io.open(json_formatted_file_path, "r") as format_file:
        json_formatted_training_data = json.load(format_file)
    os.remove(json_formatted_file_path)

    assert diff(json_formatted_training_data, training_data_only_tagger) == {}


@pytest.mark.parametrize("input_csv_file", ["data/training_data_format.csv"])
def test_cli_format_converter_only_parser(input_csv_file):
    dframe_converter = DframeConverter(
        train_path=input_csv_file, dev_path=input_csv_file, pipeline="parser"
    )
    json_formatted_file_path, pipeline = dframe_converter.convert(
        input_csv_file, dframe_converter._nlp
    )

    training_data_only_parser = [
        {
            "id": 0,
            "paragraphs": [
                {
                    "raw": "Uber blew through $1 million a week",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Uber",
                                    "tag": "NNP",
                                    "head": 1,
                                    "dep": "nsubj",
                                },
                                {
                                    "id": 1,
                                    "orth": "blew",
                                    "tag": "VBD",
                                    "head": 0,
                                    "dep": "ROOT",
                                },
                                {
                                    "id": 2,
                                    "orth": "through",
                                    "tag": "IN",
                                    "head": -1,
                                    "dep": "prt",
                                },
                                {
                                    "id": 3,
                                    "orth": "$",
                                    "tag": "$",
                                    "head": 2,
                                    "dep": "quantmod",
                                },
                                {
                                    "id": 4,
                                    "orth": "1",
                                    "tag": "CD",
                                    "head": 1,
                                    "dep": "compound",
                                },
                                {
                                    "id": 5,
                                    "orth": "million",
                                    "tag": "CD",
                                    "head": -3,
                                    "dep": "pobj",
                                },
                                {
                                    "id": 6,
                                    "orth": "a",
                                    "tag": "DT",
                                    "head": 1,
                                    "dep": "det",
                                },
                                {
                                    "id": 7,
                                    "orth": "week",
                                    "tag": "NN",
                                    "head": -2,
                                    "dep": "npadvmod",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 1,
            "paragraphs": [
                {
                    "raw": "Android Pay expands to Canada",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Android",
                                    "tag": "VB",
                                    "head": 1,
                                    "dep": "compound",
                                },
                                {
                                    "id": 1,
                                    "orth": "Pay",
                                    "tag": "NN",
                                    "head": 1,
                                    "dep": "nsubj",
                                },
                                {
                                    "id": 2,
                                    "orth": "expands",
                                    "tag": "VBZ",
                                    "head": 0,
                                    "dep": "ROOT",
                                },
                                {
                                    "id": 3,
                                    "orth": "to",
                                    "tag": "IN",
                                    "head": -1,
                                    "dep": "prep",
                                },
                                {
                                    "id": 4,
                                    "orth": "Canada",
                                    "tag": "NNP",
                                    "head": -1,
                                    "dep": "pobj",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 2,
            "paragraphs": [
                {
                    "raw": "Spotify steps up Asia expansion",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Spotify",
                                    "tag": "VB",
                                    "head": 0,
                                    "dep": "ROOT",
                                },
                                {
                                    "id": 1,
                                    "orth": "steps",
                                    "tag": "NNS",
                                    "head": -1,
                                    "dep": "dobj",
                                },
                                {
                                    "id": 2,
                                    "orth": "up",
                                    "tag": "RP",
                                    "head": -1,
                                    "dep": "prt",
                                },
                                {
                                    "id": 3,
                                    "orth": "Asia",
                                    "tag": "NNP",
                                    "head": 1,
                                    "dep": "compound",
                                },
                                {
                                    "id": 4,
                                    "orth": "expansion",
                                    "tag": "NN",
                                    "head": -4,
                                    "dep": "dobj",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 3,
            "paragraphs": [
                {
                    "raw": "Google Maps launches location sharing",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Google",
                                    "tag": "NNP",
                                    "head": 1,
                                    "dep": "compound",
                                },
                                {
                                    "id": 1,
                                    "orth": "Maps",
                                    "tag": "NNPS",
                                    "head": 1,
                                    "dep": "nsubj",
                                },
                                {
                                    "id": 2,
                                    "orth": "launches",
                                    "tag": "VBZ",
                                    "head": 0,
                                    "dep": "ROOT",
                                },
                                {
                                    "id": 3,
                                    "orth": "location",
                                    "tag": "NN",
                                    "head": 1,
                                    "dep": "compound",
                                },
                                {
                                    "id": 4,
                                    "orth": "sharing",
                                    "tag": "NN",
                                    "head": -2,
                                    "dep": "dobj",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 4,
            "paragraphs": [
                {
                    "raw": "Google rebrands its business apps",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Google",
                                    "tag": "NNP",
                                    "head": 1,
                                    "dep": "nsubj",
                                },
                                {
                                    "id": 1,
                                    "orth": "rebrands",
                                    "tag": "VBZ",
                                    "head": 0,
                                    "dep": "ROOT",
                                },
                                {
                                    "id": 2,
                                    "orth": "its",
                                    "tag": "PRP$",
                                    "head": 2,
                                    "dep": "poss",
                                },
                                {
                                    "id": 3,
                                    "orth": "business",
                                    "tag": "NN",
                                    "head": 1,
                                    "dep": "compound",
                                },
                                {
                                    "id": 4,
                                    "orth": "apps",
                                    "tag": "NNS",
                                    "head": -3,
                                    "dep": "dobj",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 5,
            "paragraphs": [
                {
                    "raw": "look what i found on google! Joy",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "look",
                                    "tag": "VB",
                                    "head": 0,
                                    "dep": "ROOT",
                                },
                                {
                                    "id": 1,
                                    "orth": "what",
                                    "tag": "WP",
                                    "head": 2,
                                    "dep": "dobj",
                                },
                                {
                                    "id": 2,
                                    "orth": "i",
                                    "tag": "PRP",
                                    "head": 1,
                                    "dep": "nsubj",
                                },
                                {
                                    "id": 3,
                                    "orth": "found",
                                    "tag": "VBD",
                                    "head": -3,
                                    "dep": "ccomp",
                                },
                                {
                                    "id": 4,
                                    "orth": "on",
                                    "tag": "IN",
                                    "head": -1,
                                    "dep": "prep",
                                },
                                {
                                    "id": 5,
                                    "orth": "google",
                                    "tag": "NNP",
                                    "head": -1,
                                    "dep": "pobj",
                                },
                                {
                                    "id": 6,
                                    "orth": "!",
                                    "tag": ".",
                                    "head": -6,
                                    "dep": "punct",
                                },
                            ]
                        },
                        {
                            "tokens": [
                                {
                                    "id": 7,
                                    "orth": "Joy",
                                    "tag": "NNP",
                                    "head": 0,
                                    "dep": "ROOT",
                                }
                            ]
                        },
                    ],
                }
            ],
        },
    ]

    with io.open(json_formatted_file_path, "r") as format_file:
        json_formatted_training_data = json.load(format_file)
    os.remove(json_formatted_file_path)

    assert diff(json_formatted_training_data, training_data_only_parser) == {}


@pytest.mark.parametrize("input_csv_file", ["data/training_data_format.csv"])
def test_cli_format_converter_only_ner(input_csv_file):
    dframe_converter = DframeConverter(
        train_path=input_csv_file, dev_path=input_csv_file, pipeline="ner"
    )
    json_formatted_file_path, pipeline = dframe_converter.convert(
        input_csv_file, dframe_converter._nlp
    )

    training_data_only_ner = [
        {
            "id": 0,
            "paragraphs": [
                {
                    "raw": "Uber blew through $1 million a week",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Uber",
                                    "tag": "NNP",
                                    "head": 1,
                                    "dep": "nsubj",
                                    "ner": "U-ORG",
                                },
                                {
                                    "id": 1,
                                    "orth": "blew",
                                    "tag": "VBD",
                                    "head": 0,
                                    "dep": "ROOT",
                                    "ner": "O",
                                },
                                {
                                    "id": 2,
                                    "orth": "through",
                                    "tag": "IN",
                                    "head": -1,
                                    "dep": "prep",
                                    "ner": "O",
                                },
                                {
                                    "id": 3,
                                    "orth": "$",
                                    "tag": "$",
                                    "head": 2,
                                    "dep": "quantmod",
                                    "ner": "O",
                                },
                                {
                                    "id": 4,
                                    "orth": "1",
                                    "tag": "CD",
                                    "head": 1,
                                    "dep": "compound",
                                    "ner": "O",
                                },
                                {
                                    "id": 5,
                                    "orth": "million",
                                    "tag": "CD",
                                    "head": -3,
                                    "dep": "pobj",
                                    "ner": "O",
                                },
                                {
                                    "id": 6,
                                    "orth": "a",
                                    "tag": "DT",
                                    "head": 1,
                                    "dep": "det",
                                    "ner": "O",
                                },
                                {
                                    "id": 7,
                                    "orth": "week",
                                    "tag": "NN",
                                    "head": -2,
                                    "dep": "npadvmod",
                                    "ner": "O",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 1,
            "paragraphs": [
                {
                    "raw": "Android Pay expands to Canada",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Android",
                                    "tag": "VB",
                                    "head": 1,
                                    "dep": "compound",
                                    "ner": "B-PRODUCT",
                                },
                                {
                                    "id": 1,
                                    "orth": "Pay",
                                    "tag": "NN",
                                    "head": 1,
                                    "dep": "nsubj",
                                    "ner": "L-PRODUCT",
                                },
                                {
                                    "id": 2,
                                    "orth": "expands",
                                    "tag": "VBZ",
                                    "head": 0,
                                    "dep": "ROOT",
                                    "ner": "O",
                                },
                                {
                                    "id": 3,
                                    "orth": "to",
                                    "tag": "IN",
                                    "head": -1,
                                    "dep": "prep",
                                    "ner": "O",
                                },
                                {
                                    "id": 4,
                                    "orth": "Canada",
                                    "tag": "NNP",
                                    "head": -1,
                                    "dep": "pobj",
                                    "ner": "-",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 2,
            "paragraphs": [
                {
                    "raw": "Spotify steps up Asia expansion",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Spotify",
                                    "tag": "VB",
                                    "head": 0,
                                    "dep": "ROOT",
                                    "ner": "-",
                                },
                                {
                                    "id": 1,
                                    "orth": "steps",
                                    "tag": "NNS",
                                    "head": -1,
                                    "dep": "dobj",
                                    "ner": "O",
                                },
                                {
                                    "id": 2,
                                    "orth": "up",
                                    "tag": "RP",
                                    "head": -1,
                                    "dep": "prt",
                                    "ner": "O",
                                },
                                {
                                    "id": 3,
                                    "orth": "Asia",
                                    "tag": "NNP",
                                    "head": 1,
                                    "dep": "compound",
                                    "ner": "U-LOC",
                                },
                                {
                                    "id": 4,
                                    "orth": "expansion",
                                    "tag": "NN",
                                    "head": -3,
                                    "dep": "dobj",
                                    "ner": "O",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 3,
            "paragraphs": [
                {
                    "raw": "Google Maps launches location sharing",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Google",
                                    "tag": "NNP",
                                    "head": 1,
                                    "dep": "compound",
                                    "ner": "B-PRODUCT",
                                },
                                {
                                    "id": 1,
                                    "orth": "Maps",
                                    "tag": "NNPS",
                                    "head": 1,
                                    "dep": "nsubj",
                                    "ner": "L-PRODUCT",
                                },
                                {
                                    "id": 2,
                                    "orth": "launches",
                                    "tag": "VBZ",
                                    "head": 0,
                                    "dep": "ROOT",
                                    "ner": "O",
                                },
                                {
                                    "id": 3,
                                    "orth": "location",
                                    "tag": "NN",
                                    "head": 1,
                                    "dep": "compound",
                                    "ner": "O",
                                },
                                {
                                    "id": 4,
                                    "orth": "sharing",
                                    "tag": "NN",
                                    "head": -2,
                                    "dep": "dobj",
                                    "ner": "O",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 4,
            "paragraphs": [
                {
                    "raw": "Google rebrands its business apps",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "Google",
                                    "tag": "NNP",
                                    "head": 1,
                                    "dep": "nsubj",
                                    "ner": "U-ORG",
                                },
                                {
                                    "id": 1,
                                    "orth": "rebrands",
                                    "tag": "VBZ",
                                    "head": 0,
                                    "dep": "ROOT",
                                    "ner": "O",
                                },
                                {
                                    "id": 2,
                                    "orth": "its",
                                    "tag": "PRP$",
                                    "head": 2,
                                    "dep": "poss",
                                    "ner": "O",
                                },
                                {
                                    "id": 3,
                                    "orth": "business",
                                    "tag": "NN",
                                    "head": 1,
                                    "dep": "compound",
                                    "ner": "O",
                                },
                                {
                                    "id": 4,
                                    "orth": "apps",
                                    "tag": "NNS",
                                    "head": -3,
                                    "dep": "dobj",
                                    "ner": "O",
                                },
                            ]
                        }
                    ],
                }
            ],
        },
        {
            "id": 5,
            "paragraphs": [
                {
                    "raw": "look what i found on google! Joy",
                    "sentences": [
                        {
                            "tokens": [
                                {
                                    "id": 0,
                                    "orth": "look",
                                    "tag": "VB",
                                    "head": 0,
                                    "dep": "ROOT",
                                    "ner": "O",
                                },
                                {
                                    "id": 1,
                                    "orth": "what",
                                    "tag": "WP",
                                    "head": 2,
                                    "dep": "dobj",
                                    "ner": "O",
                                },
                                {
                                    "id": 2,
                                    "orth": "i",
                                    "tag": "PRP",
                                    "head": 1,
                                    "dep": "nsubj",
                                    "ner": "O",
                                },
                                {
                                    "id": 3,
                                    "orth": "found",
                                    "tag": "VBD",
                                    "head": -3,
                                    "dep": "ccomp",
                                    "ner": "O",
                                },
                                {
                                    "id": 4,
                                    "orth": "on",
                                    "tag": "IN",
                                    "head": -1,
                                    "dep": "prep",
                                    "ner": "O",
                                },
                                {
                                    "id": 5,
                                    "orth": "google",
                                    "tag": "NNP",
                                    "head": -1,
                                    "dep": "pobj",
                                    "ner": "U-PRODUCT",
                                },
                                {
                                    "id": 6,
                                    "orth": "!",
                                    "tag": ".",
                                    "head": -6,
                                    "dep": "punct",
                                    "ner": "O",
                                },
                            ]
                        },
                        {
                            "tokens": [
                                {
                                    "id": 7,
                                    "orth": "Joy",
                                    "tag": "NNP",
                                    "head": 0,
                                    "dep": "ROOT",
                                    "ner": "O",
                                }
                            ]
                        },
                    ],
                }
            ],
        },
    ]

    with io.open(json_formatted_file_path, "r") as format_file:
        json_formatted_training_data = json.load(format_file)
    os.remove(json_formatted_file_path)

    assert diff(json_formatted_training_data, training_data_only_ner) == {}


@pytest.mark.parametrize("input_csv_file", ["data/training_data_format.csv"])
def test_cli_training(input_csv_file):
    dframe_trainer = DframeTrainer(
        "en", "/tmp/", input_csv_file, input_csv_file, debug_data_first=False
    )
    assert dframe_trainer.pipeline == "tagger,parser,ner"


@pytest.mark.parametrize("input_csv_file", ["data/training_data_format.csv"])
def test_cli_evaluation(input_csv_file):
    dframe_evaluator = DframeEvaluator("en_core_web_sm", input_csv_file)
    assert dframe_evaluator.pipeline == "tagger,parser,ner"


@pytest.mark.parametrize(
    "input_csv_file, dev_xls_file",
    [("data/training_data_format.csv", "data/training_data_format_xls.xls")],
)
def test_ods_training_file_format(input_csv_file, dev_xls_file):
    dframe_trainer = DframeTrainer("en", "/tmp/", input_csv_file, dev_xls_file)
    os.remove(dframe_trainer.train_path)
    os.remove(dframe_trainer.dev_path)
    assert dframe_trainer.pipeline == "tagger,parser,ner"


@pytest.mark.parametrize(
    "input_csv_file, dev_xls_file",
    [("data/training_data_format.csv", "data/training_data_format_xls.xls")],
)
def test_training_from_directory(input_csv_file, dev_xls_file):
    if not os.path.exists("/tmp/dframcy_test"):
        os.mkdir("/tmp/dframcy_test/")

    file_name, file_extension = os.path.splitext(input_csv_file)
    file_name = str(file_name.split("/")[-1])
    for i in range(10):
        shutil.copy(
            input_csv_file,
            "/tmp/dframcy_test/" + file_name + "_" + str(i) + file_extension,
        )

    file_name, file_extension = os.path.splitext(dev_xls_file)
    file_name = str(file_name.split("/")[-1])
    for i in range(10):
        shutil.copy(
            dev_xls_file,
            "/tmp/dframcy_test/" + file_name + "_" + str(i) + file_extension,
        )

    dframe_trainer = DframeTrainer(
        "en", "/tmp/", "/tmp/dframcy_test/", "/tmp/dframcy_test/"
    )
    shutil.rmtree("/tmp/dframcy_test/")
    assert dframe_trainer.pipeline == "tagger,parser,ner"


@pytest.mark.xfail  # test case supposed to fail due to very low number of training instances
@pytest.mark.parametrize("input_csv_file", ["data/training_data_format.csv"])
def test_data_debugging(input_csv_file):
    dframe_trainer = DframeTrainer(
        "en", "/tmp/", input_csv_file, input_csv_file, debug_data_first=True
    )
    dframe_trainer.begin_training()


@pytest.mark.parametrize("input_csv_file", ["data/textcat_training.csv"])
def test_cli_textcat_training(input_csv_file):
    dframe_textcat_classifier = DframeTrainClassifier(
        "/tmp/", input_csv_file, input_csv_file, n_iter=1
    )
    test_text = "This movie sucked"
    dframe_textcat_classifier.begin_training()
    doc = dframe_textcat_classifier.nlp(test_text)
    assert max(doc.cats.items(), key=operator.itemgetter(1))[0] in ["NEG", "POS"]


@pytest.mark.parametrize("input_csv_file", ["data/textcat_training.csv"])
def test_cli_textcat_training_multiclass(input_csv_file):
    if not os.path.exists("/tmp/dframcy_test"):
        os.mkdir("/tmp/dframcy_test/")
    training_csv = pd.read_csv(input_csv_file)
    random_update = training_csv.sample(frac=0.15)
    random_update["labels"] = "NEUTRAL"
    training_csv.update(random_update)
    training_csv.to_csv("/tmp/dframcy_test/textcat_multiclass_training.csv")
    dframe_textcat_classifier = DframeTrainClassifier(
        "/tmp/",
        "/tmp/dframcy_test/textcat_multiclass_training.csv",
        "/tmp/dframcy_test/textcat_multiclass_training.csv",
        n_iter=1,
    )
    test_text = "This movie sucked"
    dframe_textcat_classifier.begin_training()
    doc = dframe_textcat_classifier.nlp(test_text)
    shutil.rmtree("/tmp/dframcy_test/")
    assert max(doc.cats.items(), key=operator.itemgetter(1))[0] in [
        "NEG",
        "POS",
        "NEUTRAL",
    ]
