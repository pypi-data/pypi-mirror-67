# Release checklist

- [ ] Update Project-Id-Version in translations files `*.po`
- [ ] Update the [[changelog]]
- [ ] Apply the tag with the version number: `git tag X.Y.Z`
- [ ] Run `make clean`
- [ ] Run `make`
- [ ] Run `twine check dist/*`
- [ ] Publish to pypi: `twine check dist/*`
- [ ] Add an entry "_Unreleased version_" to the changelog
