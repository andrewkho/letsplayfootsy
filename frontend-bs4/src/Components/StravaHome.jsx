import React from "react";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

import StravaActivitiesPage from "./StravaActivitiesPage";


class StravaHome extends React.Component {
  render() {
    return (
      <Container>
        <Row>
          <h1> Welcome to Starva Stumit </h1>
        </Row>
        <Row>
          <StravaActivitiesPage />
        </Row>
      </Container>
    )
  }
}

export default StravaHome;
