import React, {Component} from 'react';
import PropTypes from 'prop-types';
import GridLayout from 'react-grid-layout';

/**
 * Grid is a dashboarding component that allows us to make resizable, draggable layouts
 */
class Grid extends Component {
  constructor(props) {
    super(props);
    this.handleOnLayoutChange = this.handleOnLayoutChange.bind(this);
  }

  /*
   * We need to fire an event whenever the layout changes. There are 2 events:
   * layout - whenever the grid is updated (drag, resize, etc.)
   * next_layout - whenever the number of items in the grid changed or the dimensions change.
   *   We can check for next_layout events to ensure we can redraw any components that need
   *   to be resized. In the case where we are listening for next_layout, the layout state
   *   gives us the previous layout so we can calculate which components need to be updated.
   */
  handleOnLayoutChange(layout) {
    let layoutChanged = false;
    if (layout.length !== this.props.layout.length) {
      console.log('number of components changed');
      layoutChanged = true;
    }
    for (let i = 0; i < layout.length; i++) {
      if (layout[i].w !== this.props.layout[i].w || layout[i].h !== this.props.layout[i].h) {
        console.log('component size changed');
        layoutChanged = true;
      }
    }

    if (layoutChanged) {
      /**
       * Firing a change on next_layout allows us to figure out if a redraw is required
       * before losing information about the previous layout
       */
      this.props.setProps({next_layout: layout});
    }
    // TODO Always firing a layout change event will allow us to dynamically save the layout,
    // but will it cause any issues getting stuck in a continuous loop?
    this.props.setProps({layout: layout});
  }

  render() {
    let childrenToRender;
    if (Array.isArray(this.props.children)) {
        // Wrap each child in a div with a key - this seems to be the easiest way to enable the 
        // grid layout component to recognise and attach to these components
        childrenToRender = this.props.children.map((child, i) => {
          return <div key={i + ""}>{child}</div>;
        });
    }
    else {
        childrenToRender = this.props.children ? [this.props.children.props.children] : null;
    }
    return (
        <GridLayout className="layout" layout={this.props.layout}
                    cols={this.props.cols} width={this.props.width} colWidth={this.props.colWidth}
                    rows={this.props.rows} height={this.props.height} rowHeight={this.props.rowHeight}

                    autoSize={this.props.autoSize} draggableHandle={this.props.draggableHandle}

                    onLayoutChange={this.handleOnLayoutChange}>

            {childrenToRender}

        </GridLayout>
    )
  }
}

Grid.propTypes = {
  /**
   * The ID used to identify this component in Dash callbacks
   */
  id: PropTypes.string,

  /**
   * A label that will be printed when this component is rendered.
   */
  label: PropTypes.string,

  /**
   * The value displayed in the input
   */
  value: PropTypes.string,

  /**
   * Dash-assigned callback that should be called whenever any of the
   * properties change
   */
  setProps: PropTypes.func,

  /**
   * children or something
   */
  children: PropTypes.node,

  /**
   * The number of columns in the grid
   */
  cols: PropTypes.number,

  /**
   * The number of rows in the grid
   */
  rows: PropTypes.number,

  /**
   * Width of each column
   */
  width: PropTypes.number,

  /**
   * Height of each row
   */
  height: PropTypes.number,

  /**
   * Column width
   * TODO Not sure if this one is declared properly
   */
  colWidth: PropTypes.number,

  /**
   * Row height
   */
  rowHeight: PropTypes.number,


  /**
   * The layout of components in the grid
   */
  layout: PropTypes.array,

  /**
   * Not to be passed through - holds
   */
  next_layout: PropTypes.array,

  /**
   * Whether to resize the grid to fit the current layout
   */
  autoSize: PropTypes.bool,

  /**
   * class name for the draggable handle component
   */
  draggableHandle: PropTypes.string
};

Grid.defaultProps = {
  layout: []
};

export default Grid;