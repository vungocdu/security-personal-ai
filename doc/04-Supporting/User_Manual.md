# User Manual — ActiveSG Ticketing System

**Document ID:** UM-ACTIVESG-001  
**Version:** 1.0.0  
**Status:** Draft  
**Date:** 2025-01-27  
**Owner:** Actiwell / Mercury Solutions  
**Applies To:** ActiveSG Ticketing System (Next.js + Supabase)  
**Related Standards:** ISO/IEC/IEEE 29148:2018 (Requirements Engineering), 42010:2011 (Architecture Description), 12207:2017 (Software Life Cycle), 15288:2015 (System Life Cycle), 25010:2011 (Product Quality), PDPA (Singapore)

---

## 1. Introduction

### 1.1 Purpose

This user manual provides comprehensive guidance for end users of the ActiveSG Ticketing System, including facility operations staff, facility managers, technicians, and headquarters personnel. The manual follows ISO/IEC/IEEE 29148:2018 requirements engineering standards to ensure clarity, traceability, and usability.

### 1.2 System Overview

The ActiveSG Ticketing System is a comprehensive facility management platform designed to support sports facility operations, featuring:

- Equipment maintenance ticket management
- Status and priority tracking with workflow automation
- Role-based access control (RBAC) with facility-level permissions
- SLA reporting and performance analytics
- Real-time notifications and audit trails

### 1.3 Prerequisites

- Modern web browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- Stable Internet connection (minimum 1 Mbps)
- Authorized user account with appropriate role assignment
- Basic web application usage knowledge
- Understanding of facility operations workflows

---

## 2. User Roles & Access Control

### 2.1 Role Definitions (ISO/IEC/IEEE 25010:2011 - Security)

| Role           | Description            | Access Scope                | Permissions                                 |
| -------------- | ---------------------- | --------------------------- | ------------------------------------------- |
| **HQ Staff**   | Headquarters personnel | System-wide, all facilities | Full CRUD operations, system administration |
| **Manager**    | Facility manager       | Assigned facilities only    | Read/Write within facility scope            |
| **Staff**      | Operations staff       | Assigned facilities only    | Limited CRUD, status updates                |
| **Technician** | Maintenance technician | Assigned equipment/tickets  | Equipment-specific access, ticket updates   |

### 2.2 Authentication Process (ISO/IEC/IEEE 29148:2018 - Security Requirements)

1. **Access**: Navigate to system URL
2. **Credentials**: Enter email and password
3. **Authentication**: System validates credentials via JWT/Supabase Auth
4. **Authorization**: Role-based permissions are assigned
5. **Redirect**: User is directed to appropriate dashboard based on role

---

## 3. Dashboard Overview (ISO/IEC/IEEE 25010:2011 - Usability)

### 3.1 Main Dashboard Components

- **KPI Cards**: Real-time performance metrics and system health indicators
- **Recent Tickets**: Latest ticket activity with status indicators
- **Quick Actions**: Contextual shortcuts for common operations
- **Notifications**: System alerts, updates, and workflow notifications
- **Performance Metrics**: SLA compliance, response times, and throughput data

### 3.2 Navigation Structure (ISO/IEC/IEEE 29148:2018 - Usability Requirements)

- **Dashboard**: Home page with role-specific widgets
- **Tickets**: Ticket management with filtering and search capabilities
- **Equipment**: Equipment inventory and maintenance tracking
- **Reports**: Analytics and reporting dashboard
- **Settings**: User preferences and system configuration

---

## 4. Ticket Management (ISO/IEC/IEEE 12207:2017 - Process Management)

### 4.1 Creating a Ticket (ISO/IEC/IEEE 29148:2018 - Functional Requirements)

1. **Navigation**: Access Tickets → Create New Ticket
2. **Required Information**:
   - **Title**: Brief description (mandatory field)
   - **Description**: Detailed information (optional)
   - **Priority**: Low/Medium/High/Urgent classification
   - **Equipment**: Associated equipment (if applicable)
   - **Facility**: Facility scope (auto-populated based on user role)
3. **Submission**: Click "Create Ticket" to submit

### 4.2 Ticket Status Workflow (ISO/IEC/IEEE 12207:2017 - Process Flow)

```
Created → In Progress → Resolved → Closed
```

**Status Transitions**:

- **Created**: Initial state after ticket creation
- **In Progress**: Work has commenced on the ticket
- **Resolved**: Issue has been addressed and verified
- **Closed**: Ticket is completed and archived

### 4.3 Viewing Tickets (ISO/IEC/IEEE 25010:2011 - Usability)

- **List View**: Paginated ticket list with sorting capabilities
- **Detail View**: Comprehensive ticket information and history
- **Filter Options**: Status, Priority, Date Range, Facility, Assignee
- **Search**: Full-text search across ticket content

### 4.4 Updating Tickets (ISO/IEC/IEEE 29148:2018 - Traceability)

- **Status Changes**: Follow defined workflow transitions
- **Comments**: Add contextual notes and updates
- **Assignment**: Assign tickets to appropriate technicians
- **Audit Trail**: All changes are logged with timestamps and user information

---

## 5. Equipment Management (ISO/IEC/IEEE 25010:2011 - Maintainability)

### 5.1 Equipment List (ISO/IEC/IEEE 29148:2018 - Functional Requirements)

- **Facility-based View**: Equipment organized by facility scope
- **Search and Filter**: Advanced filtering by equipment type, status, location
- **Status Indicators**: Visual status representation (Operational, Maintenance, Out of Service)
- **Sorting Options**: Sort by name, status, last maintenance date

### 5.2 Equipment Details (ISO/IEC/IEEE 25010:2011 - Information Quality)

- **Equipment Information**: Specifications, installation date, warranty status
- **Maintenance History**: Complete maintenance log with timestamps
- **Related Tickets**: Associated tickets and maintenance requests
- **Performance Metrics**: Uptime statistics and reliability data

---

## 6. Reports & Analytics (ISO/IEC/IEEE 25010:2011 - Performance Efficiency)

### 6.1 Available Reports (ISO/IEC/IEEE 29148:2018 - Non-Functional Requirements)

- **SLA Report**: Ticket resolution performance against service level agreements
- **Equipment Status**: Comprehensive equipment health and maintenance status
- **Performance Metrics**: System performance indicators and KPIs
- **Compliance Reports**: Regulatory and audit compliance documentation

### 6.2 Report Filters (ISO/IEC/IEEE 25010:2011 - Usability)

- **Date Range**: Custom date selection for reporting periods
- **Facility**: Filter by specific facilities or facility groups
- **Priority**: Filter by ticket priority levels
- **Status**: Filter by ticket or equipment status
- **Export Options**: PDF, Excel, CSV export formats

---

## 7. User Settings (ISO/IEC/IEEE 25010:2011 - Usability)

### 7.1 Profile Management (ISO/IEC/IEEE 29148:2018 - Security Requirements)

- **Personal Information**: Update contact details and preferences
- **Password Management**: Secure password change functionality
- **Notification Settings**: Configure alert preferences and delivery methods
- **Security Settings**: Two-factor authentication and session management

### 7.2 System Preferences (ISO/IEC/IEEE 25010:2011 - Usability)

- **Language**: Multi-language support (English, Chinese, Malay, Tamil)
- **Timezone**: Asia/Singapore timezone configuration
- **Display Settings**: Theme, layout, and accessibility options
- **Notification Preferences**: Email, SMS, and in-app notification settings

---

## 8. Security & Privacy (ISO/IEC/IEEE 25010:2011 - Security)

### 8.1 Data Protection (PDPA Singapore Compliance)

- **Personal Data Protection**: All personal data is encrypted and protected according to PDPA regulations
- **Data Subject Rights**: Users have the right to access, correct, and delete their personal data
- **Audit Trail**: All significant changes are logged with timestamps and user identification
- **Data Retention**: Personal data is retained according to legal requirements and business needs
- **Consent Management**: Clear consent mechanisms for data collection and processing

### 8.2 Security Best Practices (ISO/IEC/IEEE 29148:2018 - Security Requirements)

- **Account Security**: Never share login credentials with other users
- **Session Management**: Log out when not actively using the system
- **Password Policy**: Use strong passwords and change them regularly
- **Incident Reporting**: Report security incidents immediately to system administrators
- **Access Control**: Only access data and functions within your authorized scope

---

## 9. Troubleshooting (ISO/IEC/IEEE 15288:2015 - Support Processes)

### 9.1 Common Issues (ISO/IEC/IEEE 25010:2011 - Reliability)

| Issue                 | Solution                                                    | Escalation           |
| --------------------- | ----------------------------------------------------------- | -------------------- |
| Login failure         | Verify credentials, check account status, contact admin     | System Administrator |
| Slow page loading     | Check network connection, clear browser cache, refresh page | IT Support           |
| Missing tickets       | Verify access permissions, check filter settings            | Facility Manager     |
| Ticket creation error | Validate required fields, check system status               | Technical Support    |

### 9.2 Error Messages (ISO/IEC/IEEE 29148:2018 - Error Handling)

- **401 Unauthorized**: Authentication required or invalid credentials
- **403 Forbidden**: Insufficient permissions for requested operation
- **404 Not Found**: Requested resource does not exist
- **500 Server Error**: Internal system error, contact technical support
- **503 Service Unavailable**: System maintenance or temporary unavailability

---

## 10. Support & Contact (ISO/IEC/IEEE 15288:2015 - Support Processes)

### 10.1 Help Resources (ISO/IEC/IEEE 25010:2011 - Usability)

- **User Guide**: Comprehensive documentation with step-by-step procedures
- **FAQ**: Frequently Asked Questions with detailed answers
- **Video Tutorials**: Interactive video guides for common tasks
- **Knowledge Base**: Searchable database of solutions and procedures
- **Training Materials**: Role-specific training resources and certification programs

### 10.2 Contact Information (ISO/IEC/IEEE 12207:2017 - Support Processes)

- **Technical Support**: support@activesg.sg (Response time: 4 hours during business hours)
- **System Administrator**: admin@activesg.sg (Critical issues only)
- **Emergency Hotline**: +65-XXXX-XXXX (24/7 for critical system failures)
- **Business Hours**: Monday-Friday, 8:00 AM - 6:00 PM (Singapore Time)
- **Escalation Matrix**: Defined escalation procedures for different issue types

---

## 11. Appendices (ISO/IEC/IEEE 29148:2018 - Documentation Standards)

### A. Keyboard Shortcuts (ISO/IEC/IEEE 25010:2011 - Usability)

- **Ctrl + N**: Create new ticket
- **Ctrl + F**: Search/filter functionality
- **Ctrl + R**: Refresh current view
- **Ctrl + S**: Save current form
- **Esc**: Close dialog or cancel operation
- **Tab**: Navigate between form fields
- **Enter**: Submit form or confirm action

### B. Browser Compatibility (ISO/IEC/IEEE 25010:2011 - Compatibility)

- **Chrome**: Version 90+ (Recommended)
- **Firefox**: Version 88+
- **Safari**: Version 14+
- **Edge**: Version 90+
- **Mobile Browsers**: iOS Safari 14+, Chrome Mobile 90+

### C. Mobile Access (ISO/IEC/IEEE 25010:2011 - Usability)

- **Responsive Design**: Optimized for mobile devices and tablets
- **Touch Interface**: Touch-friendly controls and gestures
- **Offline Capabilities**: Limited offline functionality for critical operations
- **Progressive Web App**: Installable web application features

### D. Accessibility (ISO/IEC/IEEE 25010:2011 - Usability)

- **WCAG 2.1 AA Compliance**: Meets accessibility standards for users with disabilities
- **Screen Reader Support**: Compatible with assistive technologies
- **Keyboard Navigation**: Full keyboard accessibility for all functions
- **High Contrast Mode**: Enhanced visibility options
- **Text Scaling**: Support for text size adjustments

### E. Performance Requirements (ISO/IEC/IEEE 25010:2011 - Performance Efficiency)

- **Page Load Time**: < 3 seconds for initial page load
- **Response Time**: < 1 second for user interactions
- **Availability**: 99.5% uptime during business hours
- **Concurrent Users**: Support for up to 500 concurrent users
- **Data Refresh**: Real-time updates with 5-minute maximum delay

---

**Document Control**

- **Last Updated**: 2025-01-27
- **Next Review**: 2025-04-27
- **Approved By**: System Administrator
- **Distribution**: All ActiveSG Ticketing System Users

**End of User Manual**
