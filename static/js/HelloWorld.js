var HelloWorld = React.createClass({
  render: function () {
    return React.createElement(
      'div',
      null,
      'Hello World'
    );
  }
});

ReactDOM.render(React.createElement(HelloWorld, null), document.getElementById('hello_world'));

