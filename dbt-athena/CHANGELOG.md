# Changelog

- This file provides a full account of all changes to `dbt-athena`
- The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
and is generated by [Changie](https://github.com/miniscruff/changie)
- Changes are listed under the (pre-)release in which they first appear
- Subsequent releases include changes from previous releases
- "Breaking changes" listed under a version may require action from end users or external maintainers when upgrading to that version
- Do not edit this file directly. This file is auto-generated using [changie](https://github.com/miniscruff/changie)
- For details on how to document a change, see the [contributing guide](/CONTRIBUTING.md#changelog-entry)
## dbt-athena 1.9.4+mdata-emrs1 - Jun 04, 2025

### Features

- additional python_submission method for emr_serverless

## dbt-athena 1.9.4 - April 28, 2025

### Features

- Add high availability when doing full refresh on existing iceberg table ([#458](https://github.com/dbt-labs/dbt-adapters/issues/458))

### Contributors
- [@alex-antonison](https://github.com/alex-antonison) ([#458](https://github.com/dbt-labs/dbt-adapters/issues/458))


## dbt-athena 1.9.3 - April 07, 2025

### Features

- Implement microbatch incremental strategy ([#409](https://github.com/dbt-labs/dbt-adapters/issues/409))
- Add support for sample mode ([#907](https://github.com/dbt-labs/dbt-adapters/issues/907))

## dbt-athena 1.9.2 - March 07, 2025

### Features

- Implement drop_glue_database macro and method ([#408](https://github.com/dbt-labs/dbt-adapters/issues/408))

### Under the Hood

- Issue a warning to dbt-athena-community users to migrate to dbt-athena ([#879](https://github.com/dbt-labs/dbt-adapters/issues/879))

### Contributors
- [@svdimchenko](https://github.com/svdimchenko) ([#408](https://github.com/dbt-labs/dbt-adapters/issues/408))

## dbt-athena 1.9.1 - February 07, 2025

# Previous Releases

For information on prior major and minor releases, see their changelogs:

- [1.8](https://github.com/dbt-labs/dbt-athena/blob/main/CHANGELOG.md)
