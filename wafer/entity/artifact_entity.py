from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str

@dataclass
class DataValidationArtifact:...


@dataclass
class DataTransformationArtifact:...

@dataclass
class ModelTrainerArtifact:...

@dataclass
class ModelEvaluationArtifact:...

@dataclass
class ModelPusherArtifact:...


