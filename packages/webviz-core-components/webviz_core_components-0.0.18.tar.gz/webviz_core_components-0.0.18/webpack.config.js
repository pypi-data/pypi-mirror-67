const path = require("path");
const TerserJSPlugin = require("terser-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");

const packagejson = require("./package.json");

const dashLibraryName = packagejson.name.replace(/-/g, "_");

module.exports = (env, argv) => {
    let mode;

    const overrides = module.exports || {};

    // if user specified mode flag take that value
    if (argv && argv.mode) {
        mode = argv.mode;
    }

    // else if configuration object is already set (module.exports) use that value
    else if (overrides.mode) {
        mode = overrides.mode;
    }

    // else take webpack default (production)
    else {
        mode = "production";
    }

    let filename = (overrides.output || {}).filename;
    if (!filename) {
        const modeSuffix = mode === "development" ? "dev" : "min";
        filename = `${dashLibraryName}.${modeSuffix}.js`;
    }

    const entry = overrides.entry || { main: "./src/lib/index.js" };

    const devtool =
        overrides.devtool ||
        (mode === "development" ? "eval-source-map" : "none");

    const externals =
        "externals" in overrides
            ? overrides.externals
            : {
                  react: "React",
                  "react-dom": "ReactDOM",
                  "plotly.js": "Plotly",
              };

    return {
        mode,
        entry,
        output: {
            path: path.resolve(__dirname, dashLibraryName),
            filename,
            library: dashLibraryName,
            libraryTarget: "window",
        },
        optimization: {
            minimizer: [
                new TerserJSPlugin({}),
                new OptimizeCSSAssetsPlugin({}),
            ],
        },
        externals,
        plugins: [
            new MiniCssExtractPlugin({
                // Options similar to the same options in webpackOptions.output
                // all options are optional
                filename: `${dashLibraryName}.css`,
            }),
        ],
        module: {
            rules: [
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    use: {
                        loader: "babel-loader",
                    },
                },
                {
                    test: /\.css$/,
                    use: [
                        {
                            loader:
                                mode === "production"
                                    ? MiniCssExtractPlugin.loader
                                    : "style-loader",
                        },
                        "css-loader",
                    ],
                },
            ],
        },
        devtool,
    };
};
