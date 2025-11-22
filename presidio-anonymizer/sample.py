from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig
from typing import Dict


def run_anonymizer(operator_name: str, params: Dict = None):
    # Initialize the engine:
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text="My name is Bond, James Bond",
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=11, end=15, score=0.8),
            RecognizerResult(entity_type="PERSON", start=17, end=27, score=0.8),
        ],
        operators={"PERSON": OperatorConfig(operator_name, params)},
    )

    return result

def main():
    # Change the following line to test any operator:

    # output = run_anonymizer("replace", {"new_value": "BIP"})
    output = run_anonymizer("redact")
    # output = run_anonymizer("initial") # this operator is to be done in the lab
    
    print(output)


if __name__ == "__main__":
    main()

