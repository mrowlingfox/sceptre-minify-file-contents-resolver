import tempfile
import pytest

from resolver.minify_file_contents import MinifyFileContents


class TestMinifyFileContentsResolver(object):

    def setup_method(self, test_method):
        self.file_contents_resolver = MinifyFileContents(
            argument=None
        )

    def test_resolving_with_existing_file(self):
        with tempfile.NamedTemporaryFile(mode='w+') as f:
            f.write("file contents")
            f.seek(0)
            self.file_contents_resolver.argument = f.name
            result = self.file_contents_resolver.resolve()

        assert result == "file contents"

    def test_resolving_with_existing_file_multiline(self):
        with tempfile.NamedTemporaryFile(mode='w+') as f:
            contents = """
            This is a 
            Multiline file
            """
            f.write(contents)
            f.seek(0)
            self.file_contents_resolver.argument = f.name
            result = self.file_contents_resolver.resolve()

        assert result == contents

    def test_resolving_with_non_existant_file(self):
        with pytest.raises(IOError):
            self.file_contents_resolver.argument = "/non_existant_file"
            self.file_contents_resolver.resolve()

    def test_resolving_with_file_path_non_string_type(self):
        with pytest.raises(TypeError):
            self.file_contents_resolver.argument = None
            self.file_contents_resolver.resolve()
    
    def test_resolving_with_existing_js_file(self):
        with tempfile.NamedTemporaryFile(mode='w+', suffix=".js") as f:
            contents = """
            const message = "Hello";
            console.log(message)
            """
            f.write(contents)
            f.seek(0)
            self.file_contents_resolver.argument = f.name
            result = self.file_contents_resolver.resolve()

        assert result == 'const message="Hello";console.log(message)'