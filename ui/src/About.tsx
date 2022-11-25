import React from 'react'
import GitInfo from 'react-git-info/macro'

export function About() {
    const gitInfo = GitInfo()

    return (
        <>
            <h1>About</h1>
            <ul className="about-list">
                <li>
                    <strong>Application:</strong> {process.env.REACT_APP_NAME}
                </li>
                <li>
                    <strong>Version:</strong> {process.env.REACT_APP_VERSION}
                </li>
                <li>
                    <strong>React version:</strong> {React.version}
                </li>
                <li>
                    <strong>Git branch:</strong> {gitInfo.branch}
                </li>
                <li>
                    <strong>Git revision:</strong> {gitInfo.commit.hash}
                </li>
                <li>
                    <strong>Git date:</strong> {gitInfo.commit.date}
                </li>
            </ul>
        </>)
}
