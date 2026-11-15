# Service address encapsulation

The next major release removes public service-address configuration. Delete endpoint assignments, constructor options, builder calls, and environment settings from application setup. The SDK selects the service internally. API keys, calculation inputs, ayanamsa, timeouts, and transport injection continue to work.

This is a breaking change; the previous override is not retained as an alias. Assigning an arbitrary attribute in a dynamic language no longer changes request routing.

Prepared against version 1.23.30. Release this change as 2.0.0 (v2.0.0 for Go); registry publication and version updates are separate release work. Go release preparation must also update the module and import paths for semantic import versioning.
