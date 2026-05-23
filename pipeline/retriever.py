import os

try:
    import pathway as pw
    # Check if we have the real package or the empty 'stub'
    IF_REAL_PATHWAY = hasattr(pw, "io")
except ImportError:
    IF_REAL_PATHWAY = False

def setup_retriever(novels_dir: str):
    if IF_REAL_PATHWAY:
        # This part runs on the Judges' Linux machines
        return pw.io.fs.read(novels_dir, format="text", skip_noparse=True)
    else:
        # This part runs on your Windows 11 machine so you can keep working
        print("![WINDOWS COMPATIBILITY MODE]")
        print("Pathway is not natively supported on Windows Python 3.13.")
        print("Using local backup ingestion for testing...")
        
        class MockPathwayTable:
            def __init__(self, directory):
                self.data = []
                for f in os.listdir(directory):
                    if f.endswith(".txt"):
                        with open(os.path.join(directory, f), 'r', encoding='utf-8') as file:
                            self.data.append(file.read())
            def select(self, **kwargs): return self
        
        return MockPathwayTable(novels_dir)