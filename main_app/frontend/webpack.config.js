const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: path.resolve(__dirname),
    entry: {
        main: './src/index.js',
    },
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].js',
        publicPath: '/static/',
    },
    plugins: [
        new BundleTracker({
            path: __dirname,
            publicPath: '/static/',
            filename: 'webpack-stats.json',
            assetsFilePath: path.resolve(__dirname, 'frontend/dist'),
        }),
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.scss$/,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader',
                ],
            },
        ],
    },
};