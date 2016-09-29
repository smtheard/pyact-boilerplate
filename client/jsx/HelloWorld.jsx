var HelloWorld = React.createClass({
  render: function() {
    return (
      <div id="hello_world">
        Hello World
      </div>
    );
  }
});

ReactDOM.render(<HelloWorld />, document.getElementById('hello_world'));
