import React, { Component } from "react";

// importing all of these classes from reactstrap module
import {
Button,
Modal,
ModalHeader,
ModalBody,
ModalFooter,
Form,
FormGroup,
Input,
Label
} from "reactstrap";

// build a class base component
class CustomModal extends Component {
constructor(props) {
	super(props);
	this.state = {
	activeItem: this.props.activeItem
	};
}
// changes handler to check if a checkbox is checed or not
handleChange = e => {
	let { name, value } = e.target;
	if (e.target.type === "checkbox") {
	value = e.target.checked;
	}
	const activeItem = { ...this.state.activeItem, [name]: value };
	this.setState({ activeItem });
};

// rendering modal in the custommodal class received toggle and on save as props,
render() {
	const { toggle, onSave } = this.props;
	return (
	<Modal isOpen={true} toggle={toggle}>
		<ModalHeader toggle={toggle}> Event Item </ModalHeader>
		<ModalBody>
		
		<Form>

			{/* 3 formgroups
			1 title label */}
			<FormGroup>
			<Label for="title">Title</Label>
			<Input
				type="text"
				name="title"
				value={this.state.activeItem.title}
				onChange={this.handleChange}
				placeholder="Enter Task Title"
			/>
			</FormGroup>

			{/* 2 description label */}
			<FormGroup>
			<Label for="duration">Duration</Label>
			<Input
				type="text"
				name="duration"
				value={this.state.activeItem.description}
				onChange={this.handleChange}
				placeholder="Enter Task Duration(00:00:00)"
			/>
			</FormGroup>

			{/* 3 completed label */}
			<FormGroup check>
			<Label for="Block">
				<Input
				type="checkbox"
				name="block"
				checked={this.state.activeItem.completed}
				onChange={this.handleChange}
				/>
				Block?
			</Label>
			</FormGroup>
		</Form>
		</ModalBody>
		{/* create a modal footer */}
		<ModalFooter>
		<Button color="success" onClick={() => onSave(this.state.activeItem)}>
			Save
		</Button>
		</ModalFooter>
	</Modal>
	);
}
}
export default CustomModal
