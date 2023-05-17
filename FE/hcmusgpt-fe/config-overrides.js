const { override, useBabelRc } = require('customize-cra');
const NodePolyfillPlugin = require('node-polyfill-webpack-plugin');

module.exports = override(
    // eslint-disable-next-line react-hooks/rules-of-hooks
    useBabelRc(),
    (config) => {
        config.plugins.push(new NodePolyfillPlugin({ excludeAliases: ['console'] }));
        return config;
    },
);
